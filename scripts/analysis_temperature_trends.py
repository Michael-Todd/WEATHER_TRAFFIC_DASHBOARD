import pandas as pd
import mysql.connector
import os

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
high_temperature,
low_temperature
FROM weather_data
ORDER BY city, date
"""

df = pd.read_sql(query, conn)
conn.close()

df["date"] = pd.to_datetime(df["date"])

df.to_csv("city_temperature_trends", index = False)

