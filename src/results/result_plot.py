from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter

from src.const import datasets, networks


def plot_learning_history_val_metrics(plot_image_file_path, network_name, dataset_name, fit_result):
    plt.cla()
    plt.clf()
    plt.plot(fit_result.epoch, fit_result.history["val_accuracy"], 'b-', label="Dokładność")
    plt.plot(fit_result.epoch, fit_result.history["val_precision"], 'r-', label="Precyzja")
    plt.plot(fit_result.epoch, fit_result.history["val_recall"], 'g-', label="Czułość")
    plt.title(f'{networks.fully_qualified_name(network_name)} / {datasets.fully_qualified_name(dataset_name)}')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
    plt.xlabel('Epoka')
    plt.legend(['Dokładność', 'Precyzja', 'Czułość'])
    plt.savefig(plot_image_file_path, dpi=150, transparent=True)
    plt.show()


def plot_learning_history_metrics(plot_image_file_path, network_name, dataset_name, fit_result):
    plt.cla()
    plt.clf()
    plt.plot(fit_result.epoch, fit_result.history["accuracy"], 'b-', label="Dokładność")
    plt.plot(fit_result.epoch, fit_result.history["precision"], 'r-', label="Precyzja")
    plt.plot(fit_result.epoch, fit_result.history["recall"], 'g-', label="Czułość")
    plt.title(f'{networks.fully_qualified_name(network_name)} / {datasets.fully_qualified_name(dataset_name)}')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
    plt.xlabel('Epoka')
    plt.legend(['Dokładność', 'Precyzja', 'Czułość'])
    plt.savefig(plot_image_file_path, dpi=150, transparent=True)
    plt.show()


def plot_learning_history_val_loss(plot_image_file_path, network_name, dataset_name, fit_result):
    plt.cla()
    plt.clf()
    plt.plot(fit_result.epoch, fit_result.history["val_loss"], '-m')
    plt.title(f'{networks.fully_qualified_name(network_name)} / {datasets.fully_qualified_name(dataset_name)}')
    plt.ylabel('Wartość funkcji straty')
    plt.xlabel('Epoka')
    plt.savefig(plot_image_file_path, dpi=150, transparent=True)
    plt.show()


def plot_learning_history_loss(plot_image_file_path, network_name, dataset_name, fit_result):
    plt.cla()
    plt.clf()
    plt.plot(fit_result.epoch, fit_result.history["loss"], '-m')
    plt.title(f'{networks.fully_qualified_name(network_name)} / {datasets.fully_qualified_name(dataset_name)}')
    plt.ylabel('Wartość funkcji straty')
    plt.xlabel('Epoka')
    plt.savefig(plot_image_file_path, dpi=150, transparent=True)
    plt.show()

def plot_loss_comparison(plot_image_file_path, network_name, dataset_name, fit_result):
    plt.cla()
    plt.clf()
    plt.plot(fit_result.epoch, fit_result.history["loss"], '-m', label="Zbiór trenujący")
    plt.plot(fit_result.epoch, fit_result.history["val_loss"], '-b', label="Zbiór testujący")
    plt.title(f'{networks.fully_qualified_name(network_name)} / {datasets.fully_qualified_name(dataset_name)}')
    plt.ylabel('Wartość funkcji straty')
    plt.xlabel('Epoka')
    plt.legend(['Zbiór trenujący', 'Zbiór testujący'])
    plt.savefig(plot_image_file_path, dpi=150, transparent=True)
    plt.show()
