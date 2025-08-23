"""
Main U-Net training script.
"""
import argparse
import torch
from models.u_net import U-Net
from config.config import U-NetConfig
from data.data_module import U-NetDataModule
from training.trainer import U-NetTrainer

def main():
    parser = argparse.ArgumentParser(description='Train U-Net model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = U-NetConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = U-Net(config)
    data_module = U-NetDataModule(config)
    trainer = U-NetTrainer(model, config)
    
    print(f'Starting U-Net training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
