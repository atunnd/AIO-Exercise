import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdims=True)

        return x_exp/total

class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x):
        c = torch.max(x, dim = 0)
        x_exp = torch.exp(x - c.values)
        total = x_exp.sum(0, keepdims=True)
        
        return x_exp/total

if __name__ == '__main__':
    data1 = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output1 = softmax(data1)
    print(output1)

    data2 = torch.Tensor([1, 2, 3])
    softmax_stable = StableSoftmax()
    output2 = softmax_stable(data2)
    print(output2)
    