FROM python:3.9
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --deploy --system
COPY ./app ./app
CMD exec gunicorn --bind :80 --workers 1 --threads 8 app.main:app