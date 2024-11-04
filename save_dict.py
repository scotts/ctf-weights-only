import torch
import os

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.x = torch.Tensor([1, 2, 3]) # Change the numbers to what you need
        #self.numbers = torch.nn.Parameter(self.x)
        self.numbers = os.getenv("SECRET")

    def forward(self):
        return torch.sum(self.numbers)


model = Model()
torch.save(model.state_dict(), "weights.pt")
