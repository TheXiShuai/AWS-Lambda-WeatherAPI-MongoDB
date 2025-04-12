# MongoDB Atlas Preparation

---

## Initial Setup

In the **AWS-weather** cluster:

- Created a new database: `weather_lambda`
- Created a collection: `weather_data`


---

## Security

Since this is for demo and portfolio purposes, I whitelisted IP address:  
`0.0.0.0/0`  


---

## Connection String

mongodb+srv://admin:<db_password>@weather-cluster.ghznvbk.mongodb.net/?retryWrites=true&w=majority&appName=weather-cluster


---

## Next Step: AWS Setup

See the full [AWS Setup](README.aws.md) for more details on how this connects with Lambda and EventBridge.

