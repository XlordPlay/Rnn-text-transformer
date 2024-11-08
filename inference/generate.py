import torch

def generate_text(model, start_text, max_length):
    model.eval()
    generated = start_text
    # Ваш код для генерации текста
    return generated