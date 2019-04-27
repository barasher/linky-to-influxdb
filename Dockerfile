FROM python:3-slim-stretch

WORKDIR /root/linky-to-influx
RUN mkdir work
COPY . .

RUN apt-get update -qq
RUN apt-get install -qq -y wget
RUN pip install -q pylinky
RUN wget -q https://github.com/barasher/influxdb-pusher/releases/download/v1.0/pusher_v1.0_linux_386
RUN chmod u+x pusher_v1.0_linux_386

CMD [ "./run.sh" ]