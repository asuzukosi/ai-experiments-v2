"""
Main LSTM training script.
"""
import argparse
import torch
from models.lstm import LSTM
from config.config import LSTMConfig
from data.data_module import LSTMDataModule
from training.trainer import LSTMTrainer

def main():
    parser = argparse.ArgumentParser(description='Train LSTM model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = LSTMConfig()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = LSTM(config)
    data_module = LSTMDataModule(config)
    trainer = LSTMTrainer(model, config)
    
    print(f'Starting LSTM training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
