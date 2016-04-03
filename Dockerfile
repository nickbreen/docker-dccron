FROM nickbreen/cron:v1.0.0

MAINTAINER Nick Breen <nick@foobarnet.nz>

RUN apt-get update && DEBIAN_FRONEND=noninteractive apt-get install -qqy python-pip && apt-get clean

RUN pip install python-dockercloud

COPY run /etc/service/dccron/run

COPY dccron.py /opt/dccron/

ENV DOCKERCLOUD_USER="" DOCKERCLOUD_APIKEY=""
