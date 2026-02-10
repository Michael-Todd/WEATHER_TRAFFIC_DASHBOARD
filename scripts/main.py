import mysql.connector             # brings in the MySQL connector library, allowing interaction between my Python and my SQL server
import pandas as pd                # brings in the pandas library and allows me to refer to it as 'pd'
import requests                    # library allowing Python to perform HTTP/HTTPS requests, necessary for the API interactions thorughout this project
from dotenv import load_dotenv     # brings in the function that reads the .env file, allowing access to my environment variables (API keys, etc...)
import os                          # brings in operating system functionality, namely reading environment variables
import weather_utils
import database_utils

# load API keys from .env; this is the entry point so this is the only place the function need be called
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# test connections and libraries
print("Python, MySQL connector, pandas, requests, and dotenv are ready!")

# test MySQL connection, safely :)
try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    print("MySQL is connected!")
    conn.close()
except Exception as e:
    print("MySQL connection failed... :()", e)


def run_weather_job(city: str):
    # building a request URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"    # deprecated parameter usage-- location by city via built-in geocoding

    response = requests.get(url)    # sending a GET request to the API endpoint and receiving/storing response (as a Response object)
    data = response.json()    # taking the JSON text from response to my GET request and converting it to Python data structure(s)
    print(data)
    
    result = weather_utils.display_weather(data)
    #print(result)

    database_utils.insert_weather_record(result)



if __name__ == "__main__":
    run_weather_job("Terrell")
    run_weather_job("Mesquite")
    run_weather_job("Dallas")



