lenet5 = 'lenet5'
resnet50 = 'resnet50'
vgg16 = 'vgg16'
inceptionv3 = 'inceptionv3'
densenet201 = "densenet201"


def fully_qualified_name(network_name):
    if network_name == lenet5:
        return "LeNet-5"
    elif network_name == resnet50:
        return "ResNet-50"
    elif network_name == vgg16:
        return "VGG-16"
    elif network_name == inceptionv3:
        return "InceptionV3"
    elif network_name == densenet201:
        return "DenseNet-201"
    else:
        return ""
