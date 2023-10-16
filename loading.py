import kaggle as kaggle
import pandas as pd


def loadData():
    data = pd.read_csv('/kaggle/input/nasaexoplanets/cleaned_5250.csv')

    kaggle.api.authenticate()

    kaggle.api.dataset_download_files('mariajtalaka/exoplanets', path='',
                                      unzip=True)
    return data
