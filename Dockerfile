FROM python:3
MAINTAINER "Janik Luechinger janik.luechinger@uzh.ch"

COPY . /pga
WORKDIR /pga

RUN apt-get -y update && apt-get -y upgrade
RUN pip install -U pip && pip install -r requirements.txt

ENTRYPOINT [ "python", "-m", "crossover" ]

# Manual image building
# docker build -t pga-cloud-crossover .
# docker tag pga-cloud-crossover jluech/pga-cloud-crossover
# docker push jluech/pga-cloud-crossover
