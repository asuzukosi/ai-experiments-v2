"""
Main DDPM training script.
"""
import argparse
import torch
from models.ddpm import DDPM
from config.config import DDPMConfig
from data.data_module import DDPMDataModule
from training.trainer import DDPMTrainer

def main():
    parser = argparse.ArgumentParser(description='Train DDPM model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = DDPMConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = DDPM(config)
    data_module = DDPMDataModule(config)
    trainer = DDPMTrainer(model, config)
    
    print(f'Starting DDPM training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
