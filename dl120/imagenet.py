import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
import os
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image

class LocalResponseNorm(nn.Module):
    """
    local response normalization was used before batch normalization, it normalizes over local neighborhoods in feature maps, creating competition 
    between neurons outputs computed using different kernels.
    """
    def __init__(self, size: int=5, alpha: float = 0.0001, beta: float = 0.75, k: float = 2.0):
        super(LocalResponseNorm, self).__init__()
        self.size = size
        self.alpha = alpha
        self.beta = beta
        self.k = k

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return F.local_response_norm(input, self.size, self.alpha, self.beta, self.k)

class AlexNetRepresentationLearner(nn.Module):
    """
    convolutional layers of the alexnet
    the original paper used two gpus and split the network across them
    certain layers had cross-gpu connections while others did not
    here we implement the full network into a single gpu but note where the split occurs
    """
    def __init__(self):
        super(AlexNetRepresentationLearner, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=96, kernel_size=11, stride=4, padding=5)
        self.lrn1 = LocalResponseNorm()
        self.maxpool1 = nn.MaxPool2d(kernel_size=3, stride=2)
        self.conv2 = nn.Conv2d(in_channels=96, out_channels=256, kernel_size=5, padding=2)
        self.lrn2 = LocalResponseNorm()
        self.pool2 = nn.MaxPool2d(kernel_size=3, stride=2)
        self.conv3 = nn.Conv2d(in_channels=256, out_channels=384, kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(in_channels=384, out_channels=384, kernel_size=3, padding=1)
        self.conv5 = nn.Conv2d(in_channels=384, out_channels=256, kernel_size=3, padding=1)
        self.pool5 = nn.MaxPool2d(kernel_size=3, stride=2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = F.relu(self.conv1(x))
        x = self.lrn1(x)
        x = self.maxpool1(x)
        x = F.relu(self.conv2(x))
        x = self.lrn2(x)
        x = self.pool2(x)
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = F.relu(self.conv5(x))
        x = self.pool5(x)
        return x

class AlexNetClassifier(nn.Module):
    """
    the fully connected classification layers of the alexnet
    the original paper uses dropout with p=0.5 in the first two fc layers
    to prevent overfitting. this is one of the first prominent use of dropout in deep learning.
    """
    def __init__(self, num_classes: int=1000, dropout:float=0.5):
        super(AlexNetClassifier, self).__init__()
        self.fc6 = nn.Linear(in_features=(6*6*256), out_features=4096)
        self.dropout6 = nn.Dropout(p=dropout)
        self.fc7 = nn.Linear(in_features=4096, out_features=4096)
        self.dropout7 = nn.Dropout(p=dropout)
        self.fc8 = nn.Linear(in_features=4096, out_features=num_classes)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.flatten(x, 1)
        x = F.relu(self.fc6(x))
        x = self.dropout6(x)
        x = F.relu(self.fc7(x))
        x = self.dropout7(x)
        x = self.fc8(x)
        return x

class AlexNet(nn.Module):
    """
    complete alexnet architecture
    this implementation is the exact architecture from the 2012 paper
    - 5 convolutional layers with relu activation
    - max pooling at end of convolutions 1, 2 and 5
    - 3 fully connected layers
    - dropout at first two fc layers to prevent overfitting
    """
    def __init__(self, num_classes: int=1000, dropout: float=0.5):
        super(AlexNet, self).__init__()
        self.features = AlexNetRepresentationLearner()
        self.classifier = AlexNetClassifier()
        self._initialize_weights()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.classifier(x)
        return x
    
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.normal_(m.weight, 0, 0.01)
                if m.out_channels == 96 and m.in_channels == 3:
                    nn.init.constant_(m.bias, 0)
                elif m.out_channels ==  256 and m.in_channels == 96:
                    nn.init.constant_(m.bias, 1)
                elif m.out_channels == 384 and m.in_channels == 256:
                    nn.init.constant_(m.bias, 0)
                elif m.out_channels == 384 and m.in_channels == 384:
                    nn.init.constant_(m.bias, 1)
                elif m.out_channels == 256 and m.in_channels == 384:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 1)

def get_imagenet_transforms(is_training: bool=True):
    if is_training:
        return transforms.Compose([
            transforms.Resize(256),
            transforms.RandomCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1),
            transforms.RandomGrayscale(p=0.2),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    else:
        return transforms.Compose([
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

def safe_pil_loader(path):
    """Custom image loader that handles corrupted images gracefully"""
    try:
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')
    except Exception as e:
        # return a black image as fallback
        return Image.new('RGB', (224, 224), (0, 0, 0))

class AlexNetTrainer:
    def __init__(self,
                 model: nn.Module,
                 device: torch.device,
                 train_loader: DataLoader,
                 val_loader: DataLoader,
                 num_epochs: int=90,
                 learning_rate: float=0.01,
                 weight_decay: float=0.0005,
                 momentum: float=0.9,
                 lr_patience: int=10,
                 lr_factor: float=0.1):
        self.model = model
        self.device = device
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.num_epochs = num_epochs
        self.optimizer = torch.optim.SGD(
            model.parameters(),
            lr=learning_rate,
            momentum=momentum,
            weight_decay=weight_decay,
        )
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            self.optimizer,
            mode='min',
            factor=lr_factor,
            patience=lr_patience,
            verbose=True,
        )
        self.criterion = nn.CrossEntropyLoss()
        self.train_losses = []
        self.val_losses = []
        self.val_accuracies = []

    def train_epoch(self):
        self.model.train()
        total_loss = 0.0
        num_batches = len(self.train_loader)
        for batch_idx, (data, target) in enumerate(self.train_loader):
            data, target = data.to(self.device), target.to(self.device)
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item()
            # if batch_idx % 100 == 0:
            print(f"batch {batch_idx} of {num_batches} | loss: {total_loss / (batch_idx + 1):.4f}")
        avg_loss = total_loss / num_batches
        return avg_loss
    
    def validate(self):
        self.model.eval()
        total_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for data, target in self.val_loader:
                data, target = data.to(self.device), target.to(self.device)
                output = self.model(data)
                loss = self.criterion(output, target)
                total_loss += loss.item()
                _, predicted = torch.max(output.data, 1)
                total += target.size(0)
                correct += (predicted == target).sum().item()
        avg_loss = total_loss / len(self.val_loader)
        avg_accuracy = 100 * (correct / total)
        return avg_loss, avg_accuracy
    
    def save_checkpoint(self, epoch: int):
        torch.save({
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'scheduler_state_dict': self.scheduler.state_dict(),
            'train_losses': self.train_losses,
            'val_losses': self.val_losses,
            'val_accuracies': self.val_accuracies,
        }, f'checkpoint_epoch_{epoch}.pth')
    
    def train(self):
        for epoch in range(self.num_epochs):
            train_loss = self.train_epoch()
            val_loss, val_accuracy = self.validate()
            self.scheduler.step(val_loss)
            self.train_losses.append(train_loss)
            self.val_losses.append(val_loss)
            self.val_accuracies.append(val_accuracy)
            print(f"Epoch {epoch+1}/{self.num_epochs} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Accuracy: {val_accuracy:.2f}%")
            if (epoch + 1) % 10 == 0:
                self.save_checkpoint(epoch + 1)

def setup_distributed(gpu_id: int, num_gpus: int):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group('nccl', 
                            rank=gpu_id, 
                            world_size=num_gpus)

def cleanup():
    if dist.is_initialized():   
        dist.destroy_process_group()

def train_distributed_worker(gpu_id:int, num_gpus:int):
    setup_distributed(gpu_id, num_gpus)
    torch.cuda.set_device(gpu_id)
    device = torch.device(f'cuda:{gpu_id}')
    if gpu_id == 0:
        print(f"training with distributed data parallel on {num_gpus} gpus")
    model = AlexNet(num_classes=1000, dropout=0.5).to(device)
    model = DDP(model, device_ids=[gpu_id])
    train_transforms = get_imagenet_transforms(is_training=True)
    val_transforms = get_imagenet_transforms(is_training=False)
    train_dataset = datasets.ImageNet(root='/mnt/data/datasets/imagenet/imagenet2012', 
                                      split='train', transform=train_transforms,
                                      loader=safe_pil_loader)
    val_dataset = datasets.ImageNet(root='/mnt/data/datasets/imagenet/imagenet2012', 
                                    split='val', transform=val_transforms,
                                    loader=safe_pil_loader)
    train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset,
                                                                    num_replicas=num_gpus,
                                                                    rank=gpu_id,
                                                                    shuffle=True)
    val_sampler = torch.utils.data.distributed.DistributedSampler(val_dataset,
                                                                    num_replicas=num_gpus,
                                                                    rank=gpu_id)
    per_gpu_batch_size = 128 // num_gpus
    train_loader = DataLoader(dataset=train_dataset,
                              sampler=train_sampler,
                              batch_size=per_gpu_batch_size,
                              num_workers=4,
                              pin_memory=True)
    val_loader = DataLoader(dataset=val_dataset,
                            sampler=val_sampler,
                            batch_size=per_gpu_batch_size,
                            num_workers=4,
                            pin_memory=True)
    trainer = AlexNetTrainer(model=model,
                             device=device,
                             train_loader=train_loader,
                             val_loader=val_loader,
                             num_epochs=90,
                             learning_rate=0.01,
                             weight_decay=0.0005,
                             momentum=0.9,
                             lr_patience=10,
                             lr_factor=0.1)
    trainer.train()
    cleanup()

if __name__ == '__main__':
    num_gpus = torch.cuda.device_count()
    mp.spawn(
        train_distributed_worker,
        nprocs=num_gpus,
        args=(num_gpus,),
        join=True
    ) 