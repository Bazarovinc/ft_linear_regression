from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from libs import models
from libs.utils.stat_functions import linear_function
from libs.utils.work_with_files import read_dataset


def visualise_data(
    data: pd.DataFrame,
    coefs: models.Coefficients,
    km: Optional[int] = None,
    price: Optional[float] = None,
) -> None:
    plt.scatter(data.km, data.price, label='data')
    x = np.array([0, max(data.km)])
    y = linear_function(x, coefs.b0, coefs.b1)
    plt.plot(x, y, 'r', label='linear function')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Linear regression')
    if km is not None and price is not None and price != 0:
        plt.plot([km], [price], 'o', color='g', label=f'price: {price}\nkm: {km}')
    plt.legend()
    plt.show()


def visualise_train_info(lr_model: models.LinearRegressionModel) -> None:
    iteration_array = np.arange(0, lr_model.iterations, 1)
    plt.plot(
        iteration_array,
        lr_model.errors,
        label=f'iterations={lr_model.iterations}\n' f'final error: {lr_model.errors[-1]}',
    )
    plt.xlabel('iterations')
    plt.ylabel('error')
    plt.title(f'Dependence of error on iterations (learning_rate={lr_model.learning_rate})')
    plt.grid()
    plt.legend()
    plt.show()
    plt.plot(
        iteration_array,
        lr_model.determination_coefs,
        label=f'iterations={lr_model.iterations}\n'
        f'final determination: '
        f'{lr_model.determination_coefs[-1]}',
    )
    plt.xlabel('iterations')
    plt.ylabel('R^2')
    plt.title(f'Dependence of determination on iterations (learning_rate={lr_model.learning_rate})')
    plt.legend()
    plt.grid()
    plt.show()


def previsual(
    price: float, km: int, coefs: models.Coefficients, configurations: models.PredictConfigurations
) -> None:
    data = read_dataset(configurations.dataset)
    visualise_data(data, coefs, km, price)


def visualise_statistics(lr, array, type):
    plt.bar(lr, array)
    plt.xlabel('learning_rate')
    plt.ylabel('number of iterations')
    plt.title(f'Dependence of the number of iterations on learning rate ({type})')
    plt.grid()
    plt.show()
