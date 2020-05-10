import os
import shutil
from os.path import normpath, basename


class MalariaSplitter():

    def __init__(self):
        self.base_path = "/Users/igor/malaria"
        self.test_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/malaria-cells/test/"
        self.train_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/malaria-cells/train/"
        self.validate_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/malaria-cells/validate/"
        self.items = 5000
        self.train_items = self.items * 0.7
        self.test_items = self.items * 0.2
        self.validation_items = self.items * 0.1

    def split(self):
        for subdir, dirs, files in os.walk(self.base_path):
            if len(files) != 0:
                self.items = len(files)
                self.train_items = self.items * 0.7
                self.test_items = self.items * 0.2
                self.validation_items = self.items * 0.1
                image_class = basename(normpath(subdir))
                file_counter = 0

                while file_counter < self.validation_items:
                    selected_file = files[file_counter]
                    selected_file_path = self.validate_path + image_class + "/" + selected_file
                    os.makedirs(os.path.dirname(selected_file_path), exist_ok=True)
                    shutil.move(subdir + '/' + selected_file, selected_file_path)
                    file_counter = file_counter + 1

                while file_counter < (self.validation_items + self.test_items):
                    selected_file = files[file_counter]
                    selected_file_path = self.test_path + image_class + "/" + selected_file
                    os.makedirs(os.path.dirname(selected_file_path), exist_ok=True)
                    shutil.move(subdir + '/' + selected_file, selected_file_path)
                    file_counter = file_counter + 1

                while file_counter != len(files):
                    selected_file = files[file_counter]
                    selected_file_path = self.train_path + image_class + "/" + selected_file
                    os.makedirs(os.path.dirname(selected_file_path), exist_ok=True)
                    shutil.move(subdir + '/' + selected_file, selected_file_path)
                    file_counter = file_counter + 1
