from keras.preprocessing.image import ImageDataGenerator

# DatasetPartExtractor().extract('caltech101', 30)

datasets = ['caltech101', 'cat-vs-dog_10', 'cifar10', 'cifar10_10', 'mnist', 'mnist_10']

for dataset in datasets:
    print(dataset)
    trdata = ImageDataGenerator()
    traindata = trdata.flow_from_directory(
        directory="/Users/igor/Python/CNN-Architecture-Comparison/data/{}/train/".format(dataset),
        target_size=(224, 224))
    tsdata = ImageDataGenerator()
    testdata = tsdata.flow_from_directory(
        directory="/Users/igor/Python/CNN-Architecture-Comparison/data/{}/test/".format(dataset),
        target_size=(224, 224))
    vddata = ImageDataGenerator()
    validationdata = vddata.flow_from_directory(
        directory="/Users/igor/Python/CNN-Architecture-Comparison/data/{}/validate/".format(dataset),
        target_size=(224, 224))
