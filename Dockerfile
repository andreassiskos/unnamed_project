

# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

RUN apt update 
RUN apt-get install -y software-properties-common

RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"
RUN apt-get install -y graphviz graphviz-dev

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY lib/ .

# command to run on container start
ENTRYPOINT ["./entrypoint"]

