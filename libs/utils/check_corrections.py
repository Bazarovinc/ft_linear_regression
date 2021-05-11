import pandas as pd


def check_valid_data(data: pd.DataFrame) -> bool:
    if (data.dtypes.km != 'int64' and data.dtypes.km != 'float64') or (
        data.dtypes.price != 'int64' and data.dtypes.price != 'float64'
    ):
        return False
    if len(data.km) != len(data.price):
        return False
    if data.isnull().values.any():
        return False
    return True
