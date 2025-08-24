"""
Main GAT training script.
"""
import argparse
import torch
from models.gat import GAT
from config.config import GATConfig
from data.data_module import GATDataModule
from training.trainer import GATTrainer

def main():
    parser = argparse.ArgumentParser(description='Train GAT model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = GATConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = GAT(config)
    data_module = GATDataModule(config)
    trainer = GATTrainer(model, config)
    
    print(f'Starting GAT training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
