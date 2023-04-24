FROM python:3.11
WORKDIR /app

COPY ./src/* /app/
RUN pip install -r requirements.txt

CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]