FROM ubuntu:18.04
MAINTAINER Andy Rea "email@andrewrea.co.uk"
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install net-tools nginx python-pip python3-venv
RUN pip install --upgrade pip
ADD . /

RUN pip install -r /requirements.txt
RUN python3 -m venv venvs/dashtat
RUN source /venvs/dashtat/bin/activate
