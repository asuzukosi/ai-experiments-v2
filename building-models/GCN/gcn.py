"""
Main GCN training script.
"""
import argparse
import torch
from models.gcn import GCN
from config.config import GCNConfig
from data.data_module import GCNDataModule
from training.trainer import GCNTrainer

def main():
    parser = argparse.ArgumentParser(description='Train GCN model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = GCNConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = GCN(config)
    data_module = GCNDataModule(config)
    trainer = GCNTrainer(model, config)
    
    print(f'Starting GCN training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
