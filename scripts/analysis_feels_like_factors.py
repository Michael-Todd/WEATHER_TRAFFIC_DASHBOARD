import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv 

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

query = """
SELECT
city,
date,
current_temperature,
feels_like_temperature,
humidity,
wind_speed
FROM weather_data
ORDER BY city, date
"""

df = pd.read_sql(query, conn)
conn.close()

df["date"] = pd.to_datetime(df["date"])
df["temperature_difference"] = df["feels_like_temperature"] - df["current_temperature"] #positive value = feels-like temperature is higher; negative value = feels-like temperature is lower

df.to_csv("data/feels_like_factors.csv", index = False)