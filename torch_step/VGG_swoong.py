import torch
import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim

import torchvision.datasets as datasets
import torchvision.transforms as transforms

from torch.utils.data import DataLoader

import argparse

# input=224x224 image
# num_class = 1000
# 
class VGG_swoong(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.feature=nn.Sequential()
        self.classifier=nn.Sequential()

    def forward(x):
        pass

def main(args):
    print("VGG model by swoong traning")
    model=VGG_swoong()
    pass

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='This is VGG model by swoong')
    parser.add_argument('--batch_size', type=int, default=256*2)
    parser.add_argument('--learning_rate', type=float, default=0.0002)
    parser.add_argument('--num_epoch', type=int, default=10)

    args = parser.parse_args()
    # args = args.parse_args()
    main(args)