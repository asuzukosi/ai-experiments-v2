"""
Main GPT2 training script.
"""
import argparse
import torch
from models.gpt2 import GPT2
from config.config import GPT2Config
from data.data_module import GPT2DataModule
from training.trainer import GPT2Trainer

def main():
    parser = argparse.ArgumentParser(description='Train GPT2 model')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-3, help='Learning rate')
    
    args = parser.parse_args()
    
    # Setup
    config = GPT2Config()
    config.epochs = args.epochs
    config.batch_size = args.batch_size
    config.learning_rate = args.lr
    
    # Model and data
    model = GPT2(config)
    data_module = GPT2DataModule(config)
    trainer = GPT2Trainer(model, config)
    
    print(f'Starting GPT2 training for {args.epochs} epochs...')
    # TODO: Implement training loop
    
if __name__ == '__main__':
    main()
