"""
Command line interface for GAT training and inference.
"""
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='GAT CLI')
    parser.add_argument('--mode', choices=['train', 'inference'], required=True)
    parser.add_argument('--config', type=str, help='Config file path')
    
    args = parser.parse_args()
    
    if args.mode == 'train':
        print(f"Training GAT model...")
    elif args.mode == 'inference':
        print(f"Running GAT inference...")

if __name__ == '__main__':
    main()
