from libs.utils.work_with_files import open_configurations_file, read_dataset, write_data
from libs.utils.check_corrections import check_valid_data
from libs import models
from libs.utils.visualisation import visualise_data, visualise_train_info

def main():
    configurations = open_configurations_file('train_configurations.json', models.TrainConfigurations)
    data = read_dataset(configurations.dataset)
    if check_valid_data(data):
        lr_model = models.LinearRegressionModel(data.km.to_numpy(), data.price.to_numpy(), configurations)
        lr_model.train()
        coefs = write_data(lr_model, data)
        if configurations.visualisation_graphic:
            visualise_data(data, coefs)
        if configurations.visualisation_train:
            visualise_train_info(lr_model)
    else:
        print("Error! Wrong type of dataset data!")


if __name__ == '__main__':
    main()
