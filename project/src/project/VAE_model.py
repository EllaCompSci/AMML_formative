import torch
import torch.nn as nn
import torch.nn.functional as f
import torch.utils
import torch.distributions
import torchvision
import numpy as np 
import matplotlib.pyplot as plt 
import tqdm
import mnist 
import wandb


def mnist_data():
    data = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST(
            './data',
            transform=torchvision.transforms.ToTensor(),
            download=True
        ), 
        batch_size=128,
        shuffle=True
    )

    input_dim = data.shape[0]

    print(input_dim)

class Encoder(nn.Module):
    def __init__(self, latent_dim):
        super(Encoder, self).__init__()
        self.ln1 = nn.linear()





def model():
    mnist_data()
    print("working")



if __name__ == "__main__":
    model() 