import os
import pandas as pd
import plotly
import plotly.graph_objs as go
import json


def load_clean_data():

    csv_path = os.path.join("static", "hawaii_measurements.csv")
    df = pd.read_csv(csv_path)
    df = df.assign(date=pd.to_datetime(df["date"]))

    agg_s = df.groupby(df["date"].dt.year)["prcp"].mean()

    return agg_s


def make_plot():

    df = load_clean_data()

    data = [go.Bar(x=df.index, y=df.values)]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


if __name__ == "__main__":
    print(make_plot())
