import os
import requests
import pymongo
from datetime import datetime

def lambda_handler(event, context):
    api_key = os.environ['WEATHER_API_KEY']
    city = os.environ['CITY']
    mongo_uri = os.environ['MONGO_URI']
    db_name = os.environ['DB_NAME']
    collection_name = os.environ['COLLECTION']

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
    except Exception as e:
        print(f"Failed to fetch weather data: {e}")
        return {"status": "error", "message": str(e)}

    document = {
        "timestamp": datetime.utcnow().isoformat(),
        "location": weather_data["location"]["name"],
        "temperature_c": weather_data["current"]["temp_c"],
        "condition": weather_data["current"]["condition"]["text"],
        "raw_data": weather_data
    }

    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]
        result = collection.insert_one(document)
        print(f"Inserted document ID: {result.inserted_id}")
    except Exception as e:
        print(f"MongoDB insert failed: {e}")
        return {"status": "error", "message": str(e)}

    return {"status": "success", "inserted_id": str(result.inserted_id)}
