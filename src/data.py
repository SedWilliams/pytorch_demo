from datasets import load_dataset, get_dataset_split_names, Dataset
import numpy as np
import torch

# check if cuda is available and set the device accordingly
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# if no split is specified, a dict is returned
dataset_base = load_dataset("cnn_dailymail", "3.0.0", split="train[:1%]")

tensor = dataset_base.with_format("torch", device=device)

print(tensor[0])

"""
training_data = dataset["train"]
testing_data = dataset["test"]

example = training_data[0]

print(f"{example}")
"""
