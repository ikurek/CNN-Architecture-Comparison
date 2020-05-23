lenet5 = 'lenet5'
resnet50 = 'resnet50'
vgg16 = 'vgg16'


def fully_qualified_name(network_name):
    if network_name == lenet5:
        return "LeNet-5"
    elif network_name == resnet50:
        return "ResNet-50"
    elif network_name == vgg16:
        return "VGG-16"
    else:
        return ""
