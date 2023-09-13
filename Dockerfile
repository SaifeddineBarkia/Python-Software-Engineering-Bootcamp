FROM python:3.9-alpine
RUN pip install pipenv
RUN mkdir -p /usr/src/workspace/app
WORKDIR /usr/src/workspace

COPY app ./app
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["uvicorn","app.main:appi","--host","0.0.0.0","--port","8080"]
