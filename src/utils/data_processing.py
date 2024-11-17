import pandas as pd

def preprocess_data(file_path):
    # Load data
    data = pd.read_csv(file_path)
    # Example preprocessing steps
    data = data.dropna()
    return data
