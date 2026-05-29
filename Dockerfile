FROM python:3.12-slim
LABEL authors="Приложение которок поднимается само после его закрытия"
EXPOSE 8000
RUN useradd -m appuser
USER appuser
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /myservice
COPY . /myservice
CMD ["python3", "-u", "service.py"]