"""
Command line interface for PPO training and inference.
"""
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='PPO CLI')
    parser.add_argument('--mode', choices=['train', 'inference'], required=True)
    parser.add_argument('--config', type=str, help='Config file path')
    
    args = parser.parse_args()
    
    if args.mode == 'train':
        print(f"Training PPO model...")
    elif args.mode == 'inference':
        print(f"Running PPO inference...")

if __name__ == '__main__':
    main()
