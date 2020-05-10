import os
import shutil
from os.path import normpath, basename


class DatasetPartExtractor():

    def __init__(self):
        self.base_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/{}/test/"
        self.test_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/{}/test/"
        self.train_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/{}/train/"
        self.validate_path = "/Users/igor/Python/CNN-Architecture-Comparison/data/{}/validate/"

        self.items = 5000
        self.train_items = self.items * 0.7
        self.test_items = self.items * 0.2
        self.validation_items = self.items * 0.1

    def extract(self, dataset_name, percentage):
        target_dir_name = dataset_name + "_" + str(percentage)
        target_percentage_ratio = float(percentage) / 100

        target_test_dir = self.test_path.format(target_dir_name)
        source_test_dir = self.test_path.format(dataset_name)

        target_train_dir = self.train_path.format(target_dir_name)
        source_train_dir = self.train_path.format(dataset_name)

        target_validate_dir = self.validate_path.format(target_dir_name)
        source_validate_dir = self.validate_path.format(dataset_name)

        self.copy_dir_files(source_test_dir, target_test_dir, target_percentage_ratio)
        self.copy_dir_files(source_train_dir, target_train_dir, target_percentage_ratio)
        self.copy_dir_files(source_validate_dir, target_validate_dir, target_percentage_ratio)




    def copy_dir_files(self, source_path, target_path, ratio):
        for subdir, dirs, files in os.walk(source_path):
            if len(files) > 1:
                target_items = len(files) * ratio
                file_counter = 0

                while file_counter < target_items:
                    image_class = basename(normpath(subdir))
                    selected_file = files[file_counter]
                    selected_file_target_path = target_path + image_class + "/" + selected_file
                    os.makedirs(os.path.dirname(selected_file_target_path), exist_ok=True)
                    shutil.copy(subdir + '/' + selected_file, selected_file_target_path)
                    file_counter = file_counter + 1
