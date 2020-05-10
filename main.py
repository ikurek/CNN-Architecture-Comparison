from src.datasets.dataset_generators import DatasetGenerators
from src.preprocessing.extract_part_of_dataset import DatasetPartExtractor

DatasetPartExtractor().extract('malaria-cells', 5)
data = DatasetGenerators(
    name='malaria-cells_5',
    image_size=(32, 32),
    dataset_dir='./data',
    batch_size=32,
    grayscale=False
)
print()
