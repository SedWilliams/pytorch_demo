from datasets import load_dataset, get_dataset_split_names
import numpy as np
import torch

dataset_base = load_dataset("cnn_dailymail", "3.0.0")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(get_dataset_split_names("cnn_dailymail", "3.0.0"))

# if no split is specified, a dict is returned

"""
training_data = dataset["train"]
testing_data = dataset["test"]

example = training_data[0]

print(f"{example}")
"""
