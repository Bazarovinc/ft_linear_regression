#!/usr/bin/env python3
import json

import pydantic

from libs import models, templates
from libs.utils.check_corrections import check_valid_data
from libs.utils.visualisation import visualise_data, visualise_train_info
from libs.utils.work_with_files import get_json_data, read_dataset, write_data


def main() -> int:
    try:
        configurations = models.TrainConfigurations(**get_json_data('configurations/train_configurations.json'))
    except pydantic.error_wrappers.ValidationError or json.decoder.JSONDecodeError:
        print(templates.CONFIG_FILE_ERROR)
        return 1
    data = read_dataset(configurations.dataset)
    if check_valid_data(data):
        lr_model = models.LinearRegressionModel(
            data.km.to_numpy(), data.price.to_numpy(), configurations
        )
        lr_model.train()
        coefs = write_data(lr_model, data)
        print(templates.TRAIN_RESULTS.format(b0=coefs.b0, b1=coefs.b1))
        if configurations.visualisation_graphic:
            visualise_data(data, coefs)
        if configurations.visualisation_train:
            visualise_train_info(lr_model)
    else:
        print(templates.DATASET_ERROR)
        return 1
    return 0


if __name__ == '__main__':
    main()
