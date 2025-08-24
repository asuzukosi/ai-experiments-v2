"""
Data module for DDPM.
"""
import torch
from torch.utils.data import DataLoader

class DDPMDataModule:
    def __init__(self, config):
        self.config = config
        
    def setup(self):
        """Setup training and validation datasets."""
        # TODO: Implement dataset loading for DDPM
        pass
        
    def train_dataloader(self):
        """Return training dataloader."""
        # TODO: Implement training dataloader
        pass
        
    def val_dataloader(self):
        """Return validation dataloader."""
        # TODO: Implement validation dataloader
        pass
