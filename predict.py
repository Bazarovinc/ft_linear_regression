#!/usr/bin/env python3
import json
import sys
from typing import Optional

import pydantic

from libs import models
from libs.utils.make_prediction import get_prediction
from libs.utils.visualisation import previsual
from libs.utils.work_with_files import get_json_data


def get_args() -> Optional[int]:
    km = None
    if len(sys.argv) > 1:
        for arg in sys.argv:
            if arg.isdigit():
                km = int(arg)
    return km


def main() -> int:
    if (new_km := get_args()) is not None:
        if new_km < 0:
            print("Error! The number of km can't be less than 0!")
            return 1
        try:
            configurations = models.PredictConfigurations(
                **get_json_data('configurations/predict_configurations.json')
            )
        except pydantic.error_wrappers.ValidationError or json.decoder.JSONDecodeError:
            print("Error! There are some errors in configuration file!")
            return 1
        try:
            coefs = models.Coefficients(**get_json_data(configurations.coefficients_file))
        except FileNotFoundError:
            print('There is no file with coefficients!')
            return 1
        if coefs.b0 == 0 and coefs.b1 == 0:
            print(f'The car price is {coefs.b0 + coefs.b1 * new_km}')
            return 1
        price = round(get_prediction(new_km, coefs), 4)
        if price < 0:
            price = 0
        print(f'The car price is {price}')
        if configurations.visualisation:
            previsual(price, new_km, coefs, configurations)
    else:
        print('There is an error in input number!')
    return 0


if __name__ == '__main__':
    main()
