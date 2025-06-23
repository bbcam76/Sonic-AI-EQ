import torch
from torch import nn

class SpectrogramCNN(nn.Module):
    def __init__(self):
        super(SpectrogramCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(32 * 64 * 64, 128)  # Adjust based on input size
        self.fc2 = nn.Linear(128, 10)  # 10 output neurons for EQ gains

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 32 * 64 * 64)  # Flatten the tensor
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

class TemporalLSTM(nn.Module):
    def __init__(self):
        super(TemporalLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=2, hidden_size=64, num_layers=2, batch_first=True)
        self.fc = nn.Linear(64, 10)  # 10 output neurons for EQ gains

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.fc(x[:, -1, :])  # Get the last time step
        return x

class HybridModel(nn.Module):
    def __init__(self):
        super(HybridModel, self).__init__()
        self.cnn = SpectrogramCNN()
        self.lstm = TemporalLSTM()
        self.fc = nn.Linear(20, 10)  # Combine outputs from both branches

    def forward(self, spectrogram, temporal_features):
        cnn_out = self.cnn(spectrogram)
        lstm_out = self.lstm(temporal_features)
        combined = torch.cat((cnn_out, lstm_out), dim=1)
        output = self.fc(combined)
        return output