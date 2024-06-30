import torch
import torch.nn as nn


class SoftmaxFunction(nn.Module):
    def __init__(self):
        super(SoftmaxFunction, self).__init__()

    def forward(self, data):
        exps = torch.exp(data)
        return exps / torch.sum(exps)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, data):
        max_val = torch.max(data)
        exps = torch.exp(data - max_val)
        return exps / torch.sum(exps)


# Test Case
data = torch.Tensor([1, 2, 3])

# Standard Softmax
softmax = SoftmaxFunction()
output = softmax(data)
assert round(output[0].item(),2)
print("Softmax output:", output)

# Stable Softmax
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
assert round ( output [ -1]. item () , 2)
print("Stable Softmax output:", output)
