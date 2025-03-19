FROM python:3.9.5-slim
WORKDIR /app
COPY requirements/base.txt base.txt
COPY requirements/prod.txt prod.txt
RUN pip3 install -r prof.txt
COPY . .
RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT ["./docker-entrypoint.sh"]
