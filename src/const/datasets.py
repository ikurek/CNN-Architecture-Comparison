caltech101 = 'caltech101'
catvsdog = 'cat-vs-dog'
cifar10 = 'cifar10'
malaria = 'malaria-cells'
mnist = 'mnist'


def fully_qualified_name(dataset_name):
    if dataset_name == caltech101:
        return "CALTECH101"
    elif dataset_name == catvsdog:
        return "Dogs vs Cats"
    elif dataset_name == cifar10:
        return "CIFAR10"
    elif dataset_name == malaria:
        return "Malaria Cells"
    elif dataset_name == mnist:
        return "MNIST"
    else:
        return ""
