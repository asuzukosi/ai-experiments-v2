"""
Configuration for GAN model.
"""

class GANConfig:
    def __init__(self):
        # Model hyperparameters
        self.learning_rate = 1e-3
        self.batch_size = 32
        self.epochs = 100
        
        # Training settings
        self.device = 'cuda'
        self.num_workers = 4
        
        # Architecture specific parameters
        # TODO: Add GAN specific parameters
        pass
