FROM python:3.7

WORKDIR /app/web
COPY . /app/web

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "server.py"]
