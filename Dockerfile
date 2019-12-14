FROM python:3-slim-stretch

WORKDIR /root/linky-to-influx
RUN mkdir work
COPY . .

RUN apt-get update -qq \
&& apt-get install -qq -y wget \
&& rm -rf /var/lib/apt/lists/* \
&& pip install -q  -r requirements.txt \
&& wget -q -O pusher https://github.com/barasher/influxdb-pusher/releases/download/v1.1/pusher_v1.1_linux_386 \
&& chmod u+x pusher

CMD [ "./run.sh" ]
