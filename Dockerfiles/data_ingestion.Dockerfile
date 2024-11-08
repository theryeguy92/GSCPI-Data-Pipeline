FROM python:3.8-slim
WORKDIR /app
COPY ./scripts/data_ingestion.py /app
COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh
RUN pip install kafka-python pandas requests xlrd
CMD ["/app/wait-for-it.sh", "kafka_broker:9092", "--", "python", "data_ingestion.py"]