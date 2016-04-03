FROM nickbreen/cron:v1.0.0

MAINTAINER Nick Breen <nick@foobarnet.nz>

RUN apt-get update && DEBIAN_FRONEND=noninteractive apt-get install -qqy python-pip && apt-get clean

RUN pip install python-dockercloud

COPY run /etc/service/dockercloud-events/run

COPY events.py /opt/dcapi/

ENV DOCKERCLOUD_USER="" DOCKERCLOUD_APIKEY=""
