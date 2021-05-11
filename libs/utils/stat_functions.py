from typing import Union

from numpy import ndarray
from pandas import DataFrame


def error_function(x: DataFrame, y: DataFrame, estimated: DataFrame) -> float:
    return sum(pow(y - estimated, 2)) / (len(x))


def mean(array: DataFrame) -> DataFrame:
    return sum(array) / len(array)


def mse(x: DataFrame, y: DataFrame, estimated: DataFrame) -> float:
    return sum(pow(y - estimated, 2)) / (len(x))


def determination(x: DataFrame, y: DataFrame, estimated: DataFrame) -> float:
    return 1 - mse(x, y, estimated) / sum(pow(y - mean(y), 2))


def linear_function(
    x: Union[ndarray, int, float, DataFrame], b0: float, b1: float
) -> Union[ndarray, int, float, DataFrame]:
    return b0 + b1 * x
