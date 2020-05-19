import glob
import os


def clear_exported_models(model_directory):
    for file in glob.glob(f'{model_directory}*'):
        os.remove(file)
