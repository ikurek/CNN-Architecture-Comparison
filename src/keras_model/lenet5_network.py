from keras import Model
from keras.layers import Conv2D, AveragePooling2D, Flatten, Dense
from keras.models import Sequential
from keras.losses import categorical_crossentropy
from src.parameters.metrics import all


class LeNet5Network:

    def __init__(self):
        self.classes = None
        self.optimizer = 'adam'
        self.loss = categorical_crossentropy
        self.metrics = all()
        self.image_size = (32, 32)
        self.grayscale = True
        self.batch_size = 32

    def print_config(self):
        print("Loss: {}".format(self.loss))
        print("Metrics: {}".format(self.metrics))
        print("Image size: {}".format(self.image_size))
        print("Grayscale: {}".format(self.grayscale))
        print("Batch size: {}".format(self.batch_size))

    def get_compiled_model(self, classes) -> Model:
        self.classes = classes
        model = Sequential()
        model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 1)))
        model.add(AveragePooling2D())
        model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
        model.add(AveragePooling2D())
        model.add(Flatten())
        model.add(Dense(units=120, activation='relu'))
        model.add(Dense(units=84, activation='relu'))
        model.add(Dense(units=self.classes, activation='softmax'))

        model.compile(
            optimizer=self.optimizer,
            loss=self.loss,
            metrics=self.metrics,
        )

        return model
