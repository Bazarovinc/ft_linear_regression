from libs.utils.normalization import normalize_data
from random import uniform
from libs.utils.stat_functions import error_function, determination


class LinearRegressionModel:

    def __init__(self, x, y, configurations):
        self.normalized_x = normalize_data(x)
        self.normalized_y = normalize_data(y)
        self.learning_rate = configurations.learning_rate
        if configurations.coefs_start == 'zeros':
            self.b0 = 0
            self.b1 = 0
        elif configurations.coefs_start == 'random':
            self.b0 = uniform(-1.0, 1.0)
            self.b1 = uniform(-1.0, 1.0)
        self.errors = []
        self.determination_coefs = []
        self.data_size = len(x)
        self.iterations = 0

    def train(self):
        while True:
            self.iterations += 1
            estimated = self.b0 + self.b1 * self.normalized_x
            self.b0 -= (self.learning_rate / self.data_size) * sum(estimated - self.normalized_y)
            self.b1 -= (self.learning_rate / self.data_size) * sum((estimated - self.normalized_y) * self.normalized_x)
            error = error_function(self.normalized_x, self.normalized_y, estimated)
            determ_coef = determination(self.normalized_x, self.normalized_y, estimated)
            if len(self.errors) > 1 and self.errors[-1] <= error or \
                    (len(self.determination_coefs) > 1 and self.determination_coefs[-1] >= determ_coef or
                     determ_coef == 1):
                self.errors.append(error)
                self.determination_coefs.append(determ_coef)
                break
            self.errors.append(error)
            self.determination_coefs.append(determ_coef)

