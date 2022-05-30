from flask import Flask, redirect, render_template, url_for
from plots import make_plot_data
from crud import get_data

from seed_database import seed_database

app = Flask(__name__)


@app.before_first_request
def startup():
    seed_database()


@app.route("/")
def main():
    return redirect(url_for("dashboard"))


@app.route("/dashboard/")
def dashboard():
    df = get_data()
    print(df)
    plot_data = make_plot_data(df)
    return render_template("index.html", plot_data=plot_data)


if __name__ == "__main__":
    app.run(debug=True)
