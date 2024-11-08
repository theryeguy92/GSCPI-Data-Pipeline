from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('supply_chain_data', bootstrap_servers='kafka_broker:9092')
for message in consumer:
    data = json.loads(message.value.decode())
    print("Data received:", data)
    # Process data and make forecasts here