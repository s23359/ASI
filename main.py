from loading import loadData

data = loadData()
train_X, train_Y, test_X, test_Y, val_X, val_Y = process(data)
knn = train(train_X, train_Y, test_X, test_Y, val_X, val_Y)