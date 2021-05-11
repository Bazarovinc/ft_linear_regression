from pydantic import BaseSettings


class PredictConfigurations(BaseSettings):
    visualisation: bool
    coefficients_file: str
    dataset: str
