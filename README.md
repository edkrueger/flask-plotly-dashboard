# flask-plotly-dashboard

This is a demo of a simple dashboard using Flask and Plotly.  

## Database Set-up
This demo app requires a database in order to run it. The app was designed for Postgres, but with minor changes should work with SQLAlchemy supported database.  

To provision a Postgres database some options are:
* Use a cloud hosted Postgres instance such as [GCP Cloud SQL](https://cloud.google.com/sql/postgresql)
* Use the [Postgres Docker image](https://hub.docker.com/_/postgres) to run Postgres locally
* Install [Postgres](https://www.postgresql.org/) locally

## Set Environmental Variables
Pipenv will automatically set environmental variables from `.env`. We'll also use `.env` for deployment.  
* Navigate to the top level of the repo and run `cp demo.env .env` and modify `.env` to have the correct values

## Run the App Locally
Make sure that version of Python that is compatible with the version specified in `Pipfile` and Pipenv are installed.  
* To install the Python dependencies, navigate to the top level of the repo and run: `pipenv install`  
* To run the app run: `pipenv run python run_debug.py`  