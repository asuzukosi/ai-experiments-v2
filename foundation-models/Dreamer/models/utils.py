"""
Utility functions for Dreamer models.
"""
import torch

def count_parameters(model):
    """Count the number of trainable parameters in a model."""
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def save_model(model, path):
    """Save model to disk."""
    torch.save(model.state_dict(), path)
    
def load_model(model, path):
    """Load model from disk."""
    model.load_state_dict(torch.load(path))
    return model
