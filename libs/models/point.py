from pydantic import BaseModel


class PointModel(BaseModel):
    km: int
    price: int
