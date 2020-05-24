import os
import shutil
from src.const import paths
from os.path import normpath, basename


class DatasetPartExtractor:

    def __init__(self):
        self.base_path = f'{paths.data_location}{{}}/'
        self.test_path = f'{paths.data_location}{{}}/test/'
        self.train_path = f'{paths.data_location}{{}}/train/'
        self.validate_path = f'{paths.data_location}{{}}/validate/'

    # Creates new dataset from original dataset
    # Copying % ratio of elements from all classes
    def extract(self, dataset_name, percentage):
        target_dir_name = dataset_name + "_" + str(percentage)
        target_base_path = self.base_path.format(target_dir_name)
        print(f'Checking if dataset exists in {target_base_path}')
        if not os.path.exists(target_base_path):
            print(f'Extracting dataset {dataset_name} with {percentage}% rate')
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
        else:
            print(f'Dataset {dataset_name} already exists with {percentage}% rate')

    # Copies given % of elements from source to target
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
