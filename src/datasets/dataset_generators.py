from tensorflow.keras.preprocessing.image import ImageDataGenerator

import paths


class DatasetGenerators:

    def __init__(self, name, image_size, dataset_dir, batch_size, grayscale=False):
        self.name = name
        self.colormode = self.determine_color_mode(grayscale)
        self.image_size = image_size
        self.batch_size = batch_size
        self.train = self.load_train_dataset_generator()
        self.test = self.load_test_dataset_generator()
        self.validate = self.load_validate_dataset_generator()

    def determine_color_mode(self, grayscale):
        if grayscale:
            return 'grayscale'
        else:
            return 'rgb'

    def load_train_dataset_generator(self) -> ImageDataGenerator:
        print("Loading train set for {}...".format(self.name))
        return ImageDataGenerator().flow_from_directory(
            directory=r"{}{}/train".format(paths.data_location, self.name),
            target_size=self.image_size,
            color_mode=self.colormode,
            batch_size=self.batch_size
        )

    def load_test_dataset_generator(self) -> ImageDataGenerator:
        print("Loading test set for {}...".format(self.name))
        return ImageDataGenerator().flow_from_directory(
            directory=r"{}{}/test".format(paths.data_location, self.name),
            target_size=self.image_size,
            color_mode=self.colormode,
            batch_size=self.batch_size
        )

    def load_validate_dataset_generator(self) -> ImageDataGenerator:
        print("Loading validation set for {}...".format(self.name))
        return ImageDataGenerator().flow_from_directory(
            directory=r"{}{}/validate".format(paths.data_location, self.name),
            target_size=self.image_size,
            color_mode=self.colormode,
            batch_size=self.batch_size
        )
