"""
Main LeNet training script.
"""
import argparse
import torch
from models.lenet import LeNet
from config.config import LeNetConfig
from data.data_module import LeNetDataModule
from training.trainer import LeNetTrainer

def main():
    parser = argparse.ArgumentParser(description='Train LeNet model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = LeNetConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = LeNet(config)
    data_module = LeNetDataModule(config)
    trainer = LeNetTrainer(model, config)
    
    print(f'Starting LeNet training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
