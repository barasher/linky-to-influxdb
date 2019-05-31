FROM python:3-slim-stretch

WORKDIR /root/linky-to-influx
RUN mkdir work
COPY . .

RUN apt-get update -qq
RUN apt-get install -qq -y wget
RUN pip install -q  fake_useragent simplejson python-dateutil requests
RUN wget -q -O pusher https://github.com/barasher/influxdb-pusher/releases/download/v1.0/pusher_v1.0_linux_386
RUN chmod u+x pusher

CMD [ "./run.sh" ]