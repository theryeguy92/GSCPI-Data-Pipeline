# data_ingestion.py

import requests
import pandas as pd
from kafka import KafkaProducer
import json

# Pull the GSCPI data

url = 'https://www.newyorkfed.org/medialibrary/research/interactives/gscpi/downloads/gscpi_data.xlsx'


def download_gscpi_data():
    response = requests.get(url)
    with open('gscpi_data.xlsx', 'wb') as file:
        file.write(response.content)

    # Read Pulled Data

    df = pd.read_excel('gscpi_data.xlsx', sheet_name='GSCPI Monthly Data')
    print("GSCPI Data Loaded", df.head())
    return df

# init Kafka Producer
producer = KafkaProducer(boostrap_servers='kafka_broker:9092')

# Download and process GSCPI data
gscpi_data = download_gscpi_data()

# Send to Kafka
for index, row in gscpi_data.iterrows():
    data = row.to_dict()
    producer.send('supply_chain_data', json.dumps(data).encode('utf-8'))
    print("Data sent to Kafka:", data)

