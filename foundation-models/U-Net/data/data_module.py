"""
Data module for U-Net.
"""
import torch
from torch.utils.data import DataLoader

class U-NetDataModule:
    def __init__(self, config):
        self.config = config
        
    def setup(self):
        """Setup training and validation datasets."""
        # TODO: Implement dataset loading for U-Net
        pass
        
    def train_dataloader(self):
        """Return training dataloader."""
        # TODO: Implement training dataloader
        pass
        
    def val_dataloader(self):
        """Return validation dataloader."""
        # TODO: Implement validation dataloader
        pass
