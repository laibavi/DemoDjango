#FROM python:3.6
#
#ENV PYTHONUNBUFFERED 1
#
#RUN mkdir /demo
#
#WORKDIR /demo
#
#COPY requirements.txt /demo/
#
#RUN pip install — upgrade pip && pip install -r requirements.txt
#
#ADD company /demo/
#
#EXPOSE 80

#ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/