import json

import pandas as pd

from libs import models
from libs.models.coefficients import Coefficients
from libs.utils.normalization import denormalize_coefficients


def read_dataset(filename: str) -> pd.DataFrame:
    data = pd.read_csv(filename)
    return data


def write_data(lr_model: models.LinearRegressionModel, data: pd.DataFrame) -> models.Coefficients:
    b0, b1 = denormalize_coefficients(
        data.km.to_numpy(), data.price.to_numpy(), lr_model.b0, lr_model.b1
    )
    coefs = Coefficients(b0=b0, b1=b1)
    with open('coefficients.json', 'w') as output_file:
        json.dump(coefs.dict(), output_file)
    return coefs


def get_json_data(filename: str) -> dict:
    with open(filename) as json_file:
        return json.load(json_file)
