from src.datasets.dataset_generators import DatasetGenerators
from src.preprocessing.mnist_splitter import MnistSplitter
from keras.preprocessing.image import ImageDataGenerator

#MnistSplitter().split()

trdata = ImageDataGenerator()
traindata = trdata.flow_from_directory(
    directory="/Users/igor/Python/CNN-Architecture-Comparison/data/mnist/train/", target_size=(224, 224))
tsdata = ImageDataGenerator()
testdata = tsdata.flow_from_directory(directory="/Users/igor/Python/CNN-Architecture-Comparison/data/mnist/test/",
                                      target_size=(224, 224))
vddata = ImageDataGenerator()
validationdata = vddata.flow_from_directory(
    directory="/Users/igor/Python/CNN-Architecture-Comparison/data/mnist/validate/", target_size=(224, 224))
