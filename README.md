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
* Navigate to the top level of the repo and run `cp demo.env .env` and modify `.env` to have the correct values.
* Navigate to the top level of the repo and run `cp demo.env.yaml .env.yaml` and modify `.env.yaml` to have the correct values.

## Run the App Locally
Make sure that version of Python that is compatible with the version specified in `Pipfile` and Pipenv are installed.  
* To install the Python dependencies, navigate to the top level of the repo and run: `pipenv install`  
* To run the app run: `pipenv run python run_debug.py`  

## Run the App With Docker Locally
* Build the app with Docker: `docker build . -t flask-plotly-dashboard`  

Launch and kill in the foreground:
* Run the app with: `docker run -p 80:80 --env-file .env flask-plotly-dashboard`
* Kill the app by pressing ctrl+d or ctrl+c

Launch and kill in the background:
* Run the app with : `CONTAINER_ID=$(docker run -d -p 80:80 --env-file .env -d flask-plotly-dashboard)`
* Kill the app with `docker kill $CONTAINER_ID`

The app will be available at [http://0.0.0.0:80](http://0.0.0.0:80) and [http://127.0.0.1:80](http://127.0.0.1:80)

## Deploy to GCP

### Build and Deploy to GCR
You'll need to set you gcloud CLI to the project you want and deploy to GCP Cloud Build. This will upload the files, build the container remotely and upload it to GCR.  

To deploy to GCP Cloud Build:
    * To select you account and project, run `gcloud init`  
    * Set a default region  
    * Run the bash block below

```bash 
export CONTAINER_NAME=flask-plotly-dashboard
export PROJECT=$(gcloud config get-value project)
export GCR_TAG=gcr.io/$PROJECT/$CONTAINER_NAME
echo $GCR_TAG
gcloud builds submit --tag $GCR_TAG
```

### Deploy to GCP Cloud Run

```bash
export APP_NAME=$CONTAINER_NAME
gcloud run deploy $APP_NAME --image $GCR_TAG \
   --platform managed \
   --allow-unauthenticated \
   --env-vars-file=.env.yaml \
   --region us-west1 \
   --port 80
```