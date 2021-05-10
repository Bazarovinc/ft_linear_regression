from pydantic import BaseSettings


class TrainConfigurations(BaseSettings):
    learning_rate: float
    dataset: str
    coefs_start: str
    visualisation_graphic: bool
    visualisation_train: bool
