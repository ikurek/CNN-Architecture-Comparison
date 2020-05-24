from keras import Model
from keras.applications import InceptionV3
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from src.parameters.metrics import all


class InceptionV3Network:

    def __init__(self):
        self.classes = None
        self.optimizer = Adam()
        self.loss = categorical_crossentropy
        self.metrics = all()
        self.image_size = (299, 299)
        self.grayscale = False
        self.batch_size = 32

    def print_config(self):
        print("Loss: {}".format(self.loss))
        print("Metrics: {}".format(self.metrics))
        print("Image size: {}".format(self.image_size))
        print("Grayscale: {}".format(self.grayscale))
        print("Batch size: {}".format(self.batch_size))

    def get_compiled_model(self, classes) -> Model:
        self.classes = classes
        model: Model = InceptionV3(
            include_top=True,
            weights=None,
            classes=self.classes,
        )

        model.compile(
            optimizer=self.optimizer,
            loss=self.loss,
            metrics=self.metrics,
        )

        return model