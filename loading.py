import os
import shutil
if not os.path.isdir('../.kaggle'):
    os.mkdir('../.kaggle')
if not os.path.isfile('../.kaggle/kaggle.json'):
    shutil.copy("kaggle.json", "../.kaggle/kaggle.json")
import kaggle as kaggle
import pandas as pd

def loadData():
    kaggle.api.authenticate()

    data = kaggle.api.dataset_download_files(
        'adityamishraml/nasaexoplanets', path='datasets/kaggle', unzip=True)
    
    data = pd.read_csv('datasets/kaggle/cleaned_5250.csv')
    return data