import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def process(data):
    data.drop(columns={'name'}, inplace=True)

    data['discovery_year'] = data['discovery_year'].astype('category')
    data.dropna(axis=0, inplace=True)
    data.reset_index(inplace=True)
    numerical_columns = data._get_numeric_data().columns

    scaler = StandardScaler()
    scaled = pd.DataFrame(scaler.fit_transform(data[numerical_columns].to_numpy()), columns=numerical_columns)

    scaled['discovery_year'] = data['discovery_year'].astype('str')
    scaled['mass_wrt'] = data['mass_wrt']
    scaled['radius_wrt'] = data['radius_wrt']

    train_X, test_X, train_Y, test_Y = train_test_split(scaled.to_numpy(), data['planet_type'],
                                                        stratify=data['planet_type'], train_size=0.7)
    val_X, test_X, val_Y, test_Y = train_test_split(test_X, test_Y,
                                                        stratify=test_Y, train_size=0.5)
    return train_X, train_Y, test_X, test_Y, val_X, val_Y