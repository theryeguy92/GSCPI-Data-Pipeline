from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://db_dashboard:27017/")
db = client["supply_chain_db"]

@app.route('/')
def index():
    return "Supply Chain Dashboard Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)