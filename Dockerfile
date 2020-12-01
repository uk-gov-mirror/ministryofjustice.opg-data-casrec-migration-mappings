FROM python:3.8-slim-buster
COPY requirements.txt /generate/requirements.txt
RUN pip3 install -r /generate/requirements.txt
ADD app /generate/app
WORKDIR /generate/app
CMD ["echo", "NO_OP"]
