# GCN Implementation

This directory contains a complete implementation of the GCN architecture as part of the 120-day deep learning journey.

## Structure

- `cli/`: Command-line interface for training and inference
- `config/`: Configuration files and hyperparameters
- `data/`: Data loading and preprocessing modules
- `inference/`: Inference engine and utilities
- `metrics/`: Training metrics and logging
- `models/`: Model architecture implementation
- `training/`: Training loop and utilities
- `utils/`: General utilities (checkpoints, early stopping, etc.)

## Usage

### Training
```bash
python cli/main.py --mode train --config config/config.py
```

### Inference
```bash
python cli/main.py --mode inference --config config/config.py
```

## TODO

- [ ] Implement GCN architecture in `models/gcn.py`
- [ ] Set up proper data loading in `data/data_module.py`
- [ ] Configure hyperparameters in `config/config.py`
- [ ] Add evaluation metrics specific to GCN
- [ ] Create comprehensive tests
- [ ] Add documentation and examples

## References

- TODO: Add relevant papers and resources for GCN
