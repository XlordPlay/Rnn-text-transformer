import torch
import torch.nn as nn

class TransformerModel(nn.Module):
    def __init__(self, input_size, output_size, num_heads, num_layers, dropout):
        super(TransformerModel, self).__init__()
        self.transformer = nn.Transformer(d_model=input_size, nhead=num_heads, num_encoder_layers=num_layers, dropout=dropout)
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        out = self.transformer(x)
        out = self.fc(out[-1])  # Используем последний выход для классификации
        return out