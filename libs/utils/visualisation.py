import pandas as pd
from libs import models
import matplotlib.pyplot as plt
import numpy as np
from libs import models


def visualise_data(data: pd.DataFrame, coefs: models.Coefficients):
    plt.scatter(data.km, data.price, label='data')
    x = np.arange(0, max(data.km), 10)
    y = coefs.b0 + coefs.b1 * x
    plt.plot(x, y, 'r', label='linear function')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Linear regression')
    plt.legend()
    plt.show()


def visualise_train_info(lr_model: models.LinearRegressionModel):
    iteration_array = np.arange(0, lr_model.iterations, 1)
    plt.plot(iteration_array, lr_model.errors, label=f'iterations={lr_model.iterations}\n'
                                                     f'final error: {lr_model.errors[-1]}')
    plt.xlabel('iterations')
    plt.ylabel('error')
    plt.title(f'Error addiction to iterations (learning_rate={lr_model.learning_rate})')
    plt.grid()
    plt.legend()
    plt.show()
    plt.plot(iteration_array, lr_model.determination_coefs, label=f'iterations={lr_model.iterations}\n'
                                                                  f'final determination: '
                                                                  f'{lr_model.determination_coefs[-1]}')
    plt.xlabel('iterations')
    plt.ylabel('R^2')
    plt.title(f'Determination addiction to iterations (learning_rate={lr_model.learning_rate})')
    plt.legend()
    plt.grid()
    plt.show()
