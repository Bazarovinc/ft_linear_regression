from pydantic import BaseModel


class Coefficients(BaseModel):
    b0: float
    b1: float
