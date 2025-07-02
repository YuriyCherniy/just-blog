FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
EXPOSE 8000
WORKDIR /app
COPY requirements/base.txt requirements/prod.txt requirements/
RUN pip install -r requirements/prod.txt --no-cache-dir
COPY . .
RUN ["chmod", "755", "docker-entrypoint.sh"]
ENTRYPOINT [ "docker-entrypoint.sh" ]
