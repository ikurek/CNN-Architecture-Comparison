import glob
import os


# Empties model directory or creates it if it does not exist
def clear_exported_models(model_directory):
    model_dir = os.path.dirname(model_directory)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    for file in glob.glob(f'{model_directory}*'):
        if not os.path.isdir(file):
            os.remove(file)


# Returns last saved model in specified directory
def get_best_model_from_directory(best_model_directory):
    list_of_files = glob.glob(f'{best_model_directory}*.h5')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file
