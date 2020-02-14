from flask import Flask, render_template
from plot import make_plot

app = Flask(__name__)


@app.route("/")
def render_plot():
    return render_template("plotly.html", plot_json=make_plot())


if __name__ == "__main__":
    app.run(debug=True)
