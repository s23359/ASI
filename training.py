from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score

from preprocesing import scaled

def train(train_X, train_Y, test_X, test_Y, val_X, val_Y):
    knn = KNeighborsClassifier()
    knn.fit(train_X, train_Y)

    predicted = knn.predict(test_X)
    print(f"accuracy : {accuracy_score(test_Y, predicted)}")
    print(f"recall : {recall_score(test_Y, predicted, average='weighted')}")
    print(f"precision : {precision_score(test_Y, predicted, average='weighted')}")

    return(knn)