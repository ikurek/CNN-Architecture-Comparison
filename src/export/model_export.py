import glob
import os


def clear_exported_models(model_directory):
    model_dir = os.path.dirname(model_directory)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    for file in glob.glob(f'{model_directory}*'):
        os.remove(file)
