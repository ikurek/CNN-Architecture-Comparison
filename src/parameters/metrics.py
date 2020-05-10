from keras.metrics import Recall, Precision, Accuracy


def all():
    return [accuracy(), precision(), recall()]


def accuracy():
    return 'accuracy'


def precision():
    return Precision()


def recall():
    return Recall()
