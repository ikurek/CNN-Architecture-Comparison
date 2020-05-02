import os

from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.losses import categorical_crossentropy

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

trdata = ImageDataGenerator()
traindata = trdata.flow_from_directory(
    directory="/Users/igor/Python/CNN-Architecture-Comparison/data/cat-vs-dog/train/", target_size=(224, 224))
tsdata = ImageDataGenerator()
testdata = tsdata.flow_from_directory(directory="/Users/igor/Python/CNN-Architecture-Comparison/data/cat-vs-dog/test/",
                                      target_size=(224, 224))
vddata = ImageDataGenerator()
validationdata = vddata.flow_from_directory(
    directory="/Users/igor/Python/CNN-Architecture-Comparison/data/cat-vs-dog/validate/", target_size=(224, 224))

model: Model = VGG16(include_top=True, weights=None, classes=2)
model.compile(optimizer='adam', loss=categorical_crossentropy, metrics=['accuracy'])
model.fit(generator=traindata, epochs=1, validation_data=validationdata)
