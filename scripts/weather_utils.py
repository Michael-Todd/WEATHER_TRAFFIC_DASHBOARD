from datetime import datetime, timezone, timedelta

def convert_unix_to_time(timestamp, timezone_offset_seconds):
    tz = timezone(timedelta(seconds=timezone_offset_seconds))     # creates a timezone object, which always takes a timedelta object as an argument; the timedelta object is fed the offset supplied by the OpenWeather API
    local_time = datetime.fromtimestamp(timestamp, tz)            # creates a datetime object via the method .fromtimestamp, which is fed a timestamp and the timezone object above to create an aware datetime
    return local_time.strftime("%H:%M:%S")


def get_sunrise(data):
    timestamp = data["sys"]["sunrise"]
    offset = data["timezone"]
    return convert_unix_to_time(timestamp, offset)

def get_sunset(data):
    timestamp = data["sys"]["sunset"]
    offset = data["timezone"]
    return convert_unix_to_time(timestamp, offset)


def get_condition(data):
    return data["weather"][0]["main"]

def get_temperature(data):
    return data["main"]["temp"]

def get_feels_like(data):
    return data["main"]["feels_like"]

def get_humidity(data):
    return data["main"]["humidity"]

def get_high(data):
    return data["main"]["temp_max"]

def get_low(data):
    return data["main"]["temp_min"]

def get_wind(data):
    return {
            "speed": data["wind"]["speed"],
            "direction": data["wind"]["deg"]    #consider conversion
            }

def get_visibility(data):
    return data["visibility"]


def display_weather(data):
    return {
        "condition": get_condition(data),
        "temperature": get_temperature(data),
        "feels like": get_feels_like(data),
        "high": get_high(data),
        "low": get_low(data),
        "humidity": get_humidity(data),
        "wind": get_wind(data),
        "visibility": get_visibility(data),
        "sunrise": get_sunrise(data),
        "sunset": get_sunset(data)
    }

def print_display_weather(data):
    print("Condition:", get_condition(data), sep=" ")
    print("Temperature:", get_temperature(data), sep= " ")



# begin crunchers
def get_temp_diff(data):
    return get_high(data) - get_low(data)

def get_sun_diff(data):
    return "PLACEHOLDER" #Loosely, I want to do "sunset - sunrise"
# end crunchers



# Idea: Tracking sunrise/sunset and make something visual with sql/tableau