"""
Metrics tracking for DDPM training.
"""

class MetricsTracker:
    def __init__(self):
        self.metrics = {}
        
    def update(self, metrics_dict):
        """Update metrics with new values."""
        for key, value in metrics_dict.items():
            if key not in self.metrics:
                self.metrics[key] = []
            self.metrics[key].append(value)
            
    def get_average(self, metric_name):
        """Get average value for a metric."""
        if metric_name in self.metrics:
            return sum(self.metrics[metric_name]) / len(self.metrics[metric_name])
        return 0.0
        
    def reset(self):
        """Reset all metrics."""
        self.metrics = {}
