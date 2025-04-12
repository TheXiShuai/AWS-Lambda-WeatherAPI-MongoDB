# AWS Lambda + EventBridge Setup

This document explains how to configure AWS services to run a Python Lambda function **hourly** using **EventBridge Scheduler**. The function fetches weather data and inserts it into **MongoDB Atlas**.


---

## Lambda Function Setup

### Create the Lambda Function:

- **Runtime**: `Python 3.12`  
- **Architecture**: `x86_64`  
- **Permissions**: Basic Lambda + CloudWatch logging (default)

### Lambda Environment Variables:

| Key               | Value                                                                 |
|------------------|-----------------------------------------------------------------------|
| `CITY`           | Taipei                                                                |
| `COLLECTION`     | weather_data                                                          |
| `DB_NAME`        | weather_lambda                                                        |
| `MONGO_URI`      | `mongodb+srv://admin...` (connection string)                           |
| `WEATHER_API_KEY`| `2bd7864d92574903a9004808251104`                                       |


---

## Lambda Layer

Python libraries like `requests` and `pymongo` are **not built-in** to AWS Lambda, so I needed to download and package them locally before writing the code.

### Steps:
```bash
mkdir -p python
pip install requests pymongo -t python/
zip -r layer.zip python
```

After this, layer.zip can be uploaded and added in the Lambda layer:
![mongo-requests-layer](/images/2%20-%20adding-lambda-layer.png)


---

## Lambda Function Code

I wrote a Python Lambda function that:

- Fetches weather data from the WeatherAPI for a city (using the `CITY` environment variable).
- Parses the JSON to extract temperature, condition, location, and timestamp.
- Inserts that data into a MongoDB Atlas collection using `pymongo`.

### Why these imports?

- `os`: to read environment variables  
- `requests`: to make HTTP requests to the Weather API  
- `pymongo`: to connect and insert data into MongoDB Atlas  
- `datetime`: to generate a timestamp

Here is the function:  
![Lambda function](/lambda.function.py)

I manually tested the function. It worked and generated CloudWatch logs:  
![CloudWatch test log](/images/5-lambda%20test.png)

Then I verified that a document was successfully inserted into MongoDB Atlas:  
![MongoDB document](/images/6%20-%20doc-inserted.png)


---

## EventBridge Scheduler

### Created a Schedule

Used a cron expression to trigger the function hourly:  
**`cron(0 * * * ? *)`** → runs at minute 0 of every hour  
![EventBridge cron](/images/7%20-%20eventbridge.png)

### Target: Lambda Function

Set the target to be the Lambda function:  
![EventBridge target Lambda](/images/8%20-%20lambda-target.png)

### Permissions

Allowed EventBridge to invoke the Lambda function by adding a **resource-based policy**:  
![EventBridge permissions](/images/9%20-%20resource-based-policy.png)


---

## CloudWatch Logs

Confirmed that CloudWatch logs are generated every hour as expected:  
![CloudWatch logs hourly](/images/10%20-%20cloudwatch-final-logs.png)


---

## MongoDB Atlas Insertion

Checked that a new document is inserted every hour in the `weather_data` collection:  
![MongoDB Atlas insertion](/images/11%20-%20weather-data.png)


---

## **Conculsion**

This project shows how AWS Lambda, EventBridge, and MongoDB Atlas can be used together to build an automated, serverless data ingestion pipeline.




