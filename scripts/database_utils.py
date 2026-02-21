import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os      

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def insert_weather_record(data: dict):
    conn = None
    cursor = None
    """
    Expects the dictionary returned by format_weather().
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
        ON DUPLICATE KEY UPDATE
            sunrise = VALUES(sunrise),
            sunset = VALUES(sunset),
            weather_condition = VALUES(weather_condition),
            current_temperature = VALUES(current_temperature),
            feels_like_temperature = VALUES(feels_like_temperature),
            humidity = VALUES(humidity),
            high_temperature = VALUES(high_temperature),
            low_temperature = VALUES(low_temperature),
            wind_speed = VALUES(wind_speed),
            wind_direction = VALUES(wind_direction),
            visibility = VALUES(visibility);
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
