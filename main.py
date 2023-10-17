from loading import loadData
from preprocesing import process
from training import train

data = loadData()
train_X, train_Y, test_X, test_Y, val_X, val_Y = process(data)
knn = train(train_X, train_Y, test_X, test_Y, val_X, val_Y)