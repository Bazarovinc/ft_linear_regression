import numpy as np

from libs import models
from libs.utils.visualisation import visualise_statistics
from libs.utils.work_with_files import read_dataset


def run_statistics_maker():
    configurations = models.TrainConfigurations(learning_rate=0,
                                                dataset=0,
                                                coefs_start='zeros',
                                                visualisation_graphic=False,
                                                visualisation_train=False)
    lr = np.arange(0.1, 1, 0.1)
    data = read_dataset('data.csv')
    km_numpy = data.km.to_numpy()
    price_numpy = data.price.to_numpy()
    zeros_iter_array = []
    for i in lr:
        configurations.learning_rate = i
        lr_model = models.LinearRegressionModel(km_numpy, price_numpy, configurations)
        lr_model.train()
        zeros_iter_array.append(lr_model.iterations)
    random_iter_array = []
    configurations.coefs_start = 'random'
    for i in lr:
        configurations.learning_rate = i
        lr_model = models.LinearRegressionModel(km_numpy, price_numpy, configurations)
        lr_model.train()
        random_iter_array.append(lr_model.iterations)
    lr_str_array = [str(round(i, 1)) for i in lr]
    visualise_statistics(lr_str_array, zeros_iter_array, 'zeros')
    visualise_statistics(lr_str_array, random_iter_array, 'random')
