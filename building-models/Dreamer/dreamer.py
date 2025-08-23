"""
Main Dreamer training script.
"""
import argparse
import torch
from models.dreamer import Dreamer
from config.config import DreamerConfig
from data.data_module import DreamerDataModule
from training.trainer import DreamerTrainer

def main():
    parser = argparse.ArgumentParser(description='Train Dreamer model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = DreamerConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = Dreamer(config)
    data_module = DreamerDataModule(config)
    trainer = DreamerTrainer(model, config)
    
    print(f'Starting Dreamer training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
