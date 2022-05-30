import os

import numpy as np
import pandas as pd

from database import engine


def make_data():
    now = pd.Timestamp.utcnow()
    start = now - pd.Timedelta(value=60, unit="minute")
    index = pd.date_range(start=start, end=now, freq="60s")
    len_ = len(index)
    values = np.random.rand(len_)
    other_values = np.random.rand(len_)

    return pd.DataFrame(
        data={"datetime": index, "value": values, "other_value": other_values}
    )


def seed_database():
    df = make_data()
    df.to_sql("records", con=engine, if_exists="replace")
