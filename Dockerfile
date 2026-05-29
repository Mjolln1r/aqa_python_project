FROM ubuntu:latest
LABEL authors="Приложение которок поднимается само после его закрытия"
EXPOSE 8000
RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip
WORKDIR /myservice
COPY . /myservice
CMD ["python3", "-u", "service.py"]