FROM python:3.10.13-bullseye

COPY requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY src/* /app/
WORKDIR /app

ENTRYPOINT ["python", "main.py"]