"""
Main DQN training script.
"""
import argparse
import torch
from models.dqn import DQN
from config.config import DQNConfig
from data.data_module import DQNDataModule
from training.trainer import DQNTrainer

def main():
    parser = argparse.ArgumentParser(description='Train DQN model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = DQNConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = DQN(config)
    data_module = DQNDataModule(config)
    trainer = DQNTrainer(model, config)
    
    print(f'Starting DQN training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
