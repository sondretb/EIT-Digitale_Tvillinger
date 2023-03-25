from torch.utils.data import Dataset
import json
import matplotlib.pyplot as plt

class veiData(Dataset):
    def __init__(self):
        super()
        self.dataset
        self.labels
        
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, index):
        return self.dataset[index], self.label[index]
    

print("nu kör vi!")