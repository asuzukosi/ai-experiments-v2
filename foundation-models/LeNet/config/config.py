"""
Configuration for LeNet model.
"""

class LeNetConfig:
    def __init__(self):
        # Model hyperparameters
        self.learning_rate = 1e-3
        self.batch_size = 32
        self.epochs = 100
        
        # Training settings
        self.device = 'cuda'
        self.num_workers = 4
        
        # Architecture specific parameters
        # TODO: Add LeNet specific parameters
        pass
