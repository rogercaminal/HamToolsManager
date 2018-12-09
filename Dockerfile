FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN echo "Installing"
RUN pip install -r requirements.txt
ADD . /code/