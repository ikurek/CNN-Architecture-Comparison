from tensorflow.keras.preprocessing.image import ImageDataGenerator


class DatasetGenerators:

    def __init__(self, name, image_size, dataset_dir, grayscale=False):
        self.name = name
        self.colormode = self.determine_color_mode(grayscale)
        self.image_size = image_size
        self.dataset_dir = dataset_dir
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
            directory=r"{}/{}/train".format(self.dataset_dir, self.name),
            target_size=self.image_size,
            color_mode=self.colormode
        )

    def load_test_dataset_generator(self) -> ImageDataGenerator:
        print("Loading test set for {}...".format(self.name))
        return ImageDataGenerator().flow_from_directory(
            directory=r"{}/{}/test".format(self.dataset_dir, self.name),
            target_size=self.image_size,
            color_mode=self.colormode
        )

    def load_validate_dataset_generator(self) -> ImageDataGenerator:
        print("Loading validation set for {}...".format(self.name))
        return ImageDataGenerator().flow_from_directory(
            directory=r"{}/{}/validate".format(self.dataset_dir, self.name),
            target_size=self.image_size,
            color_mode=self.colormode
        )
