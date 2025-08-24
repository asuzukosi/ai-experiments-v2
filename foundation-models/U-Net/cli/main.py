"""
Command line interface for U-Net training and inference.
"""
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='U-Net CLI')
    parser.add_argument('--mode', choices=['train', 'inference'], required=True)
    parser.add_argument('--config', type=str, help='Config file path')
    
    args = parser.parse_args()
    
    if args.mode == 'train':
        print(f"Training U-Net model...")
    elif args.mode == 'inference':
        print(f"Running U-Net inference...")

if __name__ == '__main__':
    main()
