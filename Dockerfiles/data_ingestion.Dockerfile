FROM python:3.8-slim
WORKDIR /app
COPY ./scripts/data_ingestion.py /app
RUN pip install kafka-python pandas
CMD ["python", "data_ingestion.py"]