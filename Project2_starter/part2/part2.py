import json
import plotly.express as px
import pandas as pd

with open("data/forecast_5days_a.json") as json_file:
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
    "Minimum": minimum_temps
    "Maximum": maximum_temps
    "Date": dates
}
fig = px.line(df, y="Minimum", x="Date", title=f"Minimum and maximum temperatures over a {len(minimum_temps)} day period")
fig.show()


# df_a = {
#     "our_data": [123, 132, 654, 345, 125, 498],
#     "more_data": [345, 67, 176, 245, 197, 391],
#     "columns": ["a", "b", "c", "d", "e", "f"]
# }
# fig = px.line(df_a, y="our_data", x="columns")
# #fig.show()