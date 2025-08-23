"""
Main A3C training script.
"""
import argparse
import torch
from models.a3c import A3C
from config.config import A3CConfig
from data.data_module import A3CDataModule
from training.trainer import A3CTrainer

def main():
    parser = argparse.ArgumentParser(description='Train A3C model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = A3CConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = A3C(config)
    data_module = A3CDataModule(config)
    trainer = A3CTrainer(model, config)
    
    print(f'Starting A3C training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
