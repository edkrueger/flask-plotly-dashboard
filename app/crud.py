from ast import parse
import pandas as pd

from .database import engine


def get_data():

    query = """
    select datetime, value, other_value from records
    """

    return pd.read_sql_query(query, con=engine, parse_dates=["datetime"])
