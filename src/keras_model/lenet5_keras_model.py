from keras.layers import Conv2D, AveragePooling2D, Flatten, Dense
from keras.models import Model, Sequential


class LeNet5:

    def __init__(self, classes):
        self.classes = classes

    def getModel(self) -> Model:
        model = Sequential()
        model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 1)))
        model.add(AveragePooling2D())
        model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
        model.add(AveragePooling2D())
        model.add(Flatten())
        model.add(Dense(units=120, activation='relu'))
        model.add(Dense(units=84, activation='relu'))
        model.add(Dense(units=self.classes, activation='softmax'))
        return model
