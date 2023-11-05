import wandb
from wandb.sklearn import plot_precision_recall, plot_class_proportions, plot_learning_curve, plot_roc

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import pickle
from sklearn.metrics import accuracy_score, recall_score, precision_score
import pandas as pd

def train(train_X, train_Y, test_X, test_Y, val_X, val_Y, model_params):
    match model_params['model']:
        case "knn" : model = KNeighborsClassifier(n_neighbors=model_params['n_neighbors'], weights=model_params['weights'])
        case "svc" : model = SVC(probability=True)
        case "random_forest" : model = RandomForestClassifier(n_estimators=model_params['n_estimators'])
        case "naive_bayes" : model = GaussianNB()

    model.fit(train_X, train_Y)

    parameters = model.get_params()

    predicted = model.predict(test_X)
    predicted_probability = model.predict_proba(test_X)
    
    run = wandb.init(project='asi-project', config=parameters, name=model_params['name'])
    wandb.log({"accuracy": accuracy_score(test_Y, predicted), 
               "recall" : recall_score(test_Y, predicted, average='weighted'), 
               "precision" : precision_score(test_Y, predicted, average='weighted'), 
               "model name" : model_params['name']})
    
    wandb.sklearn.plot_classifier(model, train_X, test_X, train_Y, test_Y, predicted, predicted_probability, pd.unique(train_Y),
                                                         model_name=model_params['model'], feature_names=train_X.dtype.names)
    
    run.finish()

    pickle.dump(model, open('model.sav', 'wb'))
    print("Model successfully saved")