# AWS Lambda + WeatherAPI + MongoDB Atlas Project

Taipei’s weather is famously unpredictable — one moment it's sunny, the next it's pouring heavy rain. Inspired by this daily chaos, I decided to build a simple project that tracks Taipei’s weather changes over time. This project fetches live weather data every hour using [WeatherAPI](https://www.weatherapi.com/), and stores it in a **MongoDB Atlas** collection using a **serverless AWS Lambda** function. The function is triggered hourly using **Amazon EventBridge Scheduler**.


---

## Objective of this project

- Fetch current weather for **Taipei** using WeatherAPI
- Store hourly weather snapshots into a **MongoDB Atlas** collection
- Trigger everything **automatically every hour** with **EventBridge**
- Monitor execution and logs using **CloudWatch**


---

## Components

### EventBridge Scheduler
- Triggers Lambda **hourly**
- No manual cron job needed

### AWS Lambda Function
- Serverless and written in **Python 3.12**
- Reads environment variables:
  - `CITY`, `MONGO_URI`, `DB_NAME`, `COLLECTION`, `WEATHER_API_KEY`
- Makes HTTP request to WeatherAPI
- Parses temperature, weather condition, timestamp, and more
- Inserts the document into MongoDB Atlas
- Sends execution logs to **CloudWatch**

### CloudWatch Logs
- Automatically receives logs from each Lambda execution
- Useful for debugging, monitoring, and verifying successful data insertion
- Helps ensure that the function runs hourly as expected

### WeatherAPI
- REST API providing live weather data in JSON format
- Data used includes:
  - `location.name`
  - `current.temp_c`
  - `current.condition.text`
  - and more

### MongoDB Atlas
- Stores hourly weather snapshots in **JSON/BSON format**
- Database: `weather_lambda`
- Collection: `weather_data`


---

## Architecture Diagram
![Architecture Diagram](./diagrams/architecture.pdf)


---

## First step: MongoDB Atlas Setup
See the detailed steps here: [README.MongoDB.md](./readmes/README.MongoDB.md)

