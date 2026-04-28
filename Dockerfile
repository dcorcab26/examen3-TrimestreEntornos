FROM python:3.11

WORKDIR /examen

RUN pip install -r requirements.txt

CMD["python","main.py"]

