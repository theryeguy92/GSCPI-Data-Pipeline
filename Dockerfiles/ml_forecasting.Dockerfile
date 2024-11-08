FROM tensorflow/tensorflow:latest
WORKDIR /app
COPY ./scripts/forecast_model.py /app
RUN pip install kafka-python pandas
CMD ["python", "forecast_model.py"]