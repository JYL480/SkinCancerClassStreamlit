import torch
import torchvision
from torch import nn




def createModel(num_classes=5, seed=42):

    # will load the model from torch and place the trained parameters inside!

    weights = torchvision.models.ViT_B_16_Weights.DEFAULT
    transforms = weights.transforms()

    # We would have to change the output classifier from 1000 to 5

    model = torchvision.models.vit_b_16(weights=weights)

    # Freeze the layers!
    for param in model.encoder.parameters():
        param.requires_grad = False
    
    for param in model.conv_proj.parameters():
        param.requires_grad = False



    torch.manual_seed(seed)
    model.heads = nn.Sequential(
        nn.Linear(in_features=768, out_features=num_classes),
    )

    return model, transforms





