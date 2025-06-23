import torch
from torch.utils.data import Dataset

class YourDatasetClass(Dataset):
    def __init__(self, data_path):
        # Load your data here
        self.data = torch.randn(100, 10)  # Example data
        self.targets = torch.randn(100, 1)  # Example targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.targets[idx]