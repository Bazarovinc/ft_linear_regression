import pandas as pd
import json
from typing import Union, Type
from libs import models
from libs.utils.normalization import denormalize_coefficents
from libs.models.coefficients import Coefficients


def open_configurations_file(filename: str, configurations_class: Union[Type[models.TrainConfigurations]]) \
        -> Union[models.TrainConfigurations]:
    with open(filename) as json_file:
        data = json.load(json_file)
        configurations = configurations_class(**data)
        return configurations


def read_dataset(filename: str) -> pd.DataFrame:
    data = pd.read_csv(filename)
    return data


def write_data(lr_model: models.LinearRegressionModel, data: pd.DataFrame):
    b0, b1 = denormalize_coefficents(data.km.to_numpy(), data.price.to_numpy(), lr_model.b0, lr_model.b1)
    coefs = Coefficients(b0=b0, b1=b1)
    with open('coefficients.json', 'w') as output_file:
        json.dump(coefs.dict(), output_file)
    return coefs
