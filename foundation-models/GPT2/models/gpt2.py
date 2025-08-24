"""
GPT2 model implementation.
"""
import torch
import torch.nn as nn

class GPT2(nn.Module):
    def __init__(self, config):
        super(GPT2, self).__init__()
        self.config = config
        
        # TODO: Implement GPT2 architecture
        self.layers = nn.Sequential(
            # Add layers here
        )
        
    def forward(self, x):
        """Forward pass through GPT2 model."""
        # TODO: Implement forward pass
        return self.layers(x)
