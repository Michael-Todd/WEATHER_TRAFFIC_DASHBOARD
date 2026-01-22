import mysql.connector
from mysql.connector import Error
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE",
        database="weather"
    )

def insert_weather_record(data: dict):
    conn = None
    cursor = None
    """
    Expects the dictionary returned by display_weather().
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO weather_data (
            city, date, sunrise, sunset, weather_condition, current_temperature,
            feels_like_temperature, humidity, high_temperature, low_temperature,
            wind_speed, wind_direction, visibility
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        today = datetime.now().date()

        values = (
            data["city"],
            today,
            data["sunrise"],
            data["sunset"],
            data["condition"],
            data["temperature"],
            data["feels like"],
            data["humidity"],
            data["high"],
            data["low"],
            data["wind"]["speed"],
            data["wind"]["direction"],
            data["visibility"]
        )

        cursor.execute(sql, values)
        conn.commit()

        print("Weather record inserted!")

    except Error as e:
        print("DATABASE INSERT FAILED:", e)

    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()

#TODO logging instead of printing; svae raw API response to a json or text column for tracing; uniqueness constraint/index on (date) to prevent duplicates