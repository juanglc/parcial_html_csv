import pandas as pd
import os

def create_array():
    file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
    data = pd.read_csv(file_path, low_memory=False)
    array = data.values.tolist()
    return array