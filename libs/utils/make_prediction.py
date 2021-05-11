from libs import models
from libs.utils.stat_functions import linear_function


def get_prediction(km: int, coefs: models.Coefficients) -> float:
    return linear_function(km, coefs.b0, coefs.b1)
