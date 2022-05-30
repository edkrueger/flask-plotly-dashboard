import json

import plotly.express as px
from plotly.utils import PlotlyJSONEncoder

styling_kwargs = {"template": "plotly_dark"}


def _fig_to_json(fig):
    return json.dumps(fig, cls=PlotlyJSONEncoder)


def make_plot_data(df):

    print(df)

    fig = px.line(df, x="datetime", y=["value", "other_value"], **styling_kwargs)

    return _fig_to_json(fig)
