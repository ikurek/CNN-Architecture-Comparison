import os
import shutil


class DogVsCatSplitter():

    def __init__(self):
        self.base_path = "/Users/igor/train/"
        self.test_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/cat-vs-dog/test/"
        self.train_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/cat-vs-dog/train/"
        self.validate_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/cat-vs-dog/validate/"
        self.items = 25000
        self.train_items = self.items * 0.7
        self.test_items = self.items * 0.2
        self.validation_items = self.items * 0.1
        self.catCount = 0
        self.dogCount = 0

    def split(self):
        for filename in os.listdir(self.base_path):
            if filename.startswith("cat"):
                self.moveCat(filename)
                self.catCount = self.catCount + 1
            elif filename.startswith("dog"):
                self.moveDog(filename)
                self.dogCount = self.dogCount + 1
            else:
                continue

    def moveCat(self, catFile):
        if self.catCount < self.validation_items / 2:
            shutil.move(self.base_path + catFile, self.validate_path + "cat/" + catFile)
        elif self.catCount < (self.test_items + self.validation_items) / 2:
            shutil.move(self.base_path + catFile, self.test_path + "cat/" + catFile)
        else:
            shutil.move(self.base_path + catFile, self.train_path + "cat/" + catFile)

    def moveDog(self, dogFile):
        if self.dogCount < self.validation_items / 2:
            shutil.move(self.base_path + dogFile, self.validate_path + "dog/" + dogFile)
        elif self.dogCount < (self.test_items + self.validation_items) / 2:
            shutil.move(self.base_path + dogFile, self.test_path + "dog/" + dogFile)
        else:
            shutil.move(self.base_path + dogFile, self.train_path + "dog/" + dogFile)
