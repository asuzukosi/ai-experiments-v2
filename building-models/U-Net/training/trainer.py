"""
Training module for U-Net.
"""
import torch
import torch.nn as nn
from torch.optim import Adam

class U-NetTrainer:
    def __init__(self, model, config):
        self.model = model
        self.config = config
        self.optimizer = Adam(model.parameters(), lr=config.learning_rate)
        self.criterion = nn.CrossEntropyLoss()  # Adjust based on task
        
    def train_epoch(self, dataloader):
        """Train for one epoch."""
        self.model.train()
        total_loss = 0.0
        
        for batch_idx, (data, target) in enumerate(dataloader):
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
            
        return total_loss / len(dataloader)
        
    def validate(self, dataloader):
        """Validate the model."""
        self.model.eval()
        total_loss = 0.0
        correct = 0
        
        with torch.no_grad():
            for data, target in dataloader:
                output = self.model(data)
                total_loss += self.criterion(output, target).item()
                pred = output.argmax(dim=1, keepdim=True)
                correct += pred.eq(target.view_as(pred)).sum().item()
                
        return total_loss / len(dataloader), correct / len(dataloader.dataset)
