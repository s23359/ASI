from sklearn.model_selection import train_test_split
import pickle

from autogluon.tabular import TabularPredictor
import pandas as pd
import numpy as np
import numpy as np
import pandas as pd


def autogluonTraining(data):
    train_X, test_X = train_test_split(pd.DataFrame(data))

    predictor = TabularPredictor(label='planet_type').fit(pd.DataFrame(train_X))
    predictions = predictor.predict(pd.DataFrame(test_X))
    
    return predictor
