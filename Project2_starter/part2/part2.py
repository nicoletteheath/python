import json
from datetime import datetime
import plotly.express as px
import pandas as pd

with open("data/forecast_10days.json") as json_file:
    forecast_data = json.load(json_file)


def convert_f_to_c(temp_in_farenheit):
    celsius_temperature_conversion = (float(temp_in_farenheit - 32.0)) * 5.0 / 9.0
    celsius_temperature = round(celsius_temperature_conversion,1)
    return celsius_temperature

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


minimum_temps = []
maximum_temps = []
minimum_real_feel = []
minimum_real_feel_shade = []
dates = []

for data in forecast_data["DailyForecasts"]:
    minimum_temps.append(convert_f_to_c(data["Temperature"]["Minimum"]["Value"]))
    maximum_temps.append(convert_f_to_c(data["Temperature"]["Maximum"]["Value"]))
    dates.append(convert_date(data["Date"]))
    minimum_real_feel.append(convert_f_to_c(data["RealFeelTemperature"]["Minimum"]["Value"]))
    minimum_real_feel_shade.append(convert_f_to_c(data["RealFeelTemperatureShade"]["Minimum"]["Value"]))


df = {
    "Minimum": minimum_temps,
    "Maximum": maximum_temps,
    "Date": dates
}
fig = px.line(df, y=["Minimum", "Maximum"], x="Date", title=f"Minimum and maximum temperatures over a {len(minimum_temps)} day period")
fig.show()

df = {
    "Minimum": minimum_temps,
    "Minimum Real Feel": minimum_real_feel,
    "Minimum Real Feel Shade": minimum_real_feel_shade,
    "Date": dates
}

fig = px.line(
    df, 
    y=["Minimum","Minimum Real Feel","Minimum Real Feel Shade"], 
    x="Date", 
    title=f"Minimum, minimum real feel and minimum real feel shade temperatures over a {len(minimum_temps)} day period")
fig.show()

