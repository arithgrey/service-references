FROM python:3.10-alpine

WORKDIR /app

COPY Pipfile Pipfile.lock /app

RUN pip install -U pipenv

RUN pipenv install --system

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
