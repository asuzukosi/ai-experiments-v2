"""
Main MaskRCNN training script.
"""
import argparse
import torch
from models.maskrcnn import MaskRCNN
from config.config import MaskRCNNConfig
from data.data_module import MaskRCNNDataModule
from training.trainer import MaskRCNNTrainer

def main():
    parser = argparse.ArgumentParser(description='Train MaskRCNN model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = MaskRCNNConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = MaskRCNN(config)
    data_module = MaskRCNNDataModule(config)
    trainer = MaskRCNNTrainer(model, config)
    
    print(f'Starting MaskRCNN training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
