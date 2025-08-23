"""
Main PointNet training script.
"""
import argparse
import torch
from models.pointnet import PointNet
from config.config import PointNetConfig
from data.data_module import PointNetDataModule
from training.trainer import PointNetTrainer

def main():
    parser = argparse.ArgumentParser(description='Train PointNet model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = PointNetConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = PointNet(config)
    data_module = PointNetDataModule(config)
    trainer = PointNetTrainer(model, config)
    
    print(f'Starting PointNet training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
