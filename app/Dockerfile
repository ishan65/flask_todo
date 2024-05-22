FROM python:3.9-slim
WORKDIR /usr/src/app
VOLUME /usr/src/app
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install Flask-SQLAlchemy
RUN pip install PyMySQL
CMD ["python", "web.py"]
