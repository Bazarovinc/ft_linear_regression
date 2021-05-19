#!/usr/bin/env python3
import json
import sys
from typing import Optional

import pydantic

from libs import models, templates
from libs.utils.make_prediction import get_prediction
from libs.utils.stat_functions import linear_function
from libs.utils.visualisation import previsual
from libs.utils.work_with_files import get_json_data


def get_args() -> Optional[int]:
    km = None
    if len(sys.argv) > 1:
        for arg in sys.argv:
            try:
                km = int(arg)
            except ValueError:
                pass
    return km


def main() -> int:
    if (new_km := get_args()) is not None:
        if new_km < 0:
            print(templates.NEGATIVE_ERROR)
            return 1
        try:
            configurations = models.PredictConfigurations(
                **get_json_data('configurations/predict_configurations.json')
            )
        except pydantic.error_wrappers.ValidationError or json.decoder.JSONDecodeError:
            print(templates.CONFIG_FILE_ERROR)
            return 1
        try:
            coefs = models.Coefficients(**get_json_data(configurations.coefficients_file))
        except FileNotFoundError:
            print(templates.NO_FILE_ERROR)
            return 1
        if coefs.b0 == 0 and coefs.b1 == 0:
            print(templates.PREDICT.format(price=linear_function(new_km, coefs.b0, coefs.b1)))
            return 1
        price = round(get_prediction(new_km, coefs), 2)
        if price < 0:
            price = 0
        print(templates.PREDICT.format(price=price))
        if configurations.visualisation and price != 0:
            previsual(price, new_km, coefs, configurations)
    else:
        print(templates.INPUT_NUMBER_ERROR)
    return 0


if __name__ == '__main__':
    main()
