FROM ubuntu
RUN apt-get update 
RUN apt-get install -y python3.11* python3-pip 
WORKDIR /usr/src/app
VOLUME /usr/src/app
RUN pip install  --break-system-packages -r requirements_dev.txt 
CMD ["python3", "web.py"]
