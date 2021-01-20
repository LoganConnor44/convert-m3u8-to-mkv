FROM python:3

WORKDIR /usr/src/app
RUN mkdir ./temp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install ffmpeg -y

COPY . .

ENTRYPOINT [ "python", "./convert-m3u8-to-mkv.py" ]