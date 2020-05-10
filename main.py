from src.preprocessing.extract_part_of_dataset import DatasetPartExtractor

DatasetPartExtractor().extract('caltech101', 40)
DatasetPartExtractor().extract('cat-vs-dog', 10)
DatasetPartExtractor().extract('cifar10', 5)
DatasetPartExtractor().extract('mnist', 5)
