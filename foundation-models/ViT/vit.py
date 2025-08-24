"""
Main ViT training script.
"""
import argparse
import torch
from models.vit import ViT
from config.config import ViTConfig
from data.data_module import ViTDataModule
from training.trainer import ViTTrainer

def main():
    parser = argparse.ArgumentParser(description='Train ViT model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = ViTConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = ViT(config)
    data_module = ViTDataModule(config)
    trainer = ViTTrainer(model, config)
    
    print(f'Starting ViT training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
