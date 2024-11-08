# Dockerfiles/db_dashboard.Dockerfile
FROM python:3.8
WORKDIR /app
COPY ./scripts/dashboard.py /app/dashboard.py
RUN pip install flask pymongo
CMD ["python", "dashboard.py"]
