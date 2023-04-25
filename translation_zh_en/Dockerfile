FROM python:3.11
WORKDIR /app

COPY ./src/* /app/
RUN pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]