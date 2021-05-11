from random import uniform
from typing import List

import pandas as pd

from libs.models.train_comfigurations import TrainConfigurations
from libs.utils.normalization import normalize_data
from libs.utils.stat_functions import (determination, error_function,
                                       linear_function)


class LinearRegressionModel:
    def __init__(self, x: pd.DataFrame, y: pd.DataFrame, configurations: TrainConfigurations):
        self.normalized_x: pd.DataFrame = normalize_data(x)
        self.normalized_y: pd.DataFrame = normalize_data(y)
        self.learning_rate: float = configurations.learning_rate
        if configurations.coefs_start == 'zeros':
            self.b0: float = 0
            self.b1: float = 0
        elif configurations.coefs_start == 'random':
            self.b0 = uniform(-1.0, 1.0)
            self.b1 = uniform(-1.0, 1.0)
        self.errors: List[float] = []
        self.determination_coefs: List[float] = []
        self.data_size: int = len(x)
        self.iterations: int = 0

    def train(self) -> None:
        while True:
            self.iterations += 1
            estimated = linear_function(self.normalized_x, self.b0, self.b1)
            self.b0 -= (self.learning_rate / self.data_size) * sum(estimated - self.normalized_y)
            self.b1 -= (self.learning_rate / self.data_size) * sum(
                (estimated - self.normalized_y) * self.normalized_x
            )
            error = error_function(self.normalized_x, self.normalized_y, estimated)
            determ_coef = determination(self.normalized_x, self.normalized_y, estimated)
            if (
                len(self.errors) > 1
                and self.errors[-1] <= error
                or (
                    len(self.determination_coefs) > 1
                    and self.determination_coefs[-1] >= determ_coef
                    or determ_coef == 1
                )
            ):
                self.errors.append(error)
                self.determination_coefs.append(determ_coef)
                break
            self.errors.append(error)
            self.determination_coefs.append(determ_coef)
