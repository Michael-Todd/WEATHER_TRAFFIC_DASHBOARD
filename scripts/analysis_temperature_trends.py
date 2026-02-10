import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "YOUR_PASSWORD_HERE",
    database = "weather"
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
terrell_df = df[df["city"] == "Terrell"]
dallas_df = df[df["city"] == "Dallas"]
mesquite_df = df[df["city"] == "Mesquite"]

terrell_df.to_csv("terrell_temperature_trends.csv", index = False)
dallas_df.to_csv("dallas_temperature_trends.csv", index = False)
mesquite_df.to_csv("mesquite_temperature_trends.csv", index = False)

