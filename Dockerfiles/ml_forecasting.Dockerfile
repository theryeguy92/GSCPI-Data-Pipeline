FROM tensorflow/tensorflow:latest
WORKDIR /app
COPY ./scripts/forecast_model.py /app
COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh
RUN pip install kafka-python pandas
CMD ["/app/wait-for-it.sh", "kafka_broker:9092", "--", "python", "forecast_model.py"]