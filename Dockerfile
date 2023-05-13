FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./main-docker.py ./

ADD images ./images 

CMD [ "python", "./main-docker.py"]