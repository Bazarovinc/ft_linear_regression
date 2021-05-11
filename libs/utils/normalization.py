from typing import Tuple, Union

import pandas as pd


def normalize_data(data: Union[pd.DataFrame, list]) -> Union[pd.DataFrame, list]:
    return (data - min(data)) / (max(data) - min(data))


def denormalize_coefficients(
    x: pd.DataFrame, y: pd.DataFrame, b0: float, b1: float
) -> Tuple[float, float]:
    denorm_b1 = (max(y) - min(y)) * b1 / (max(x) - min(x))
    denorm_b0 = min(y) + ((max(y) - min(y)) * b0) + denorm_b1 * (1 - min(x))
    return denorm_b0, denorm_b1
