import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    
    celsius_temperature_conversion = (float(temp_in_farenheit - 32.0)) * 5.0 / 9.0
    celsius_temperature = round(celsius_temperature_conversion,1)
    return celsius_temperature


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = round((total / num_items),1)
    return mean


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
       forecast_data = json.load(json_file)
  


    minimum_temps = []
    maximum_temps = []
    dates = []
    day_long_phase = []
    day_chance_rain = []
    night_long_phase = []
    night_chance_rain = []
    coldest_temp = None
    coldest_day = ""
    highest_temp = None
    highest_day = ""
    output = []


    for data in forecast_data["DailyForecasts"]:
        minimum_temps.append(convert_f_to_c(data["Temperature"]["Minimum"]["Value"]))
        maximum_temps.append(convert_f_to_c(data["Temperature"]["Maximum"]["Value"]))
        dates.append(convert_date(data["Date"]))
        day_long_phase.append(data["Day"]["LongPhrase"])
        day_chance_rain.append(data["Day"]["RainProbability"])
        night_long_phase.append(data["Night"]["LongPhrase"])
        night_chance_rain.append(data["Night"]["RainProbability"])
        if coldest_temp is None:
            coldest_temp = convert_f_to_c(data["Temperature"]["Minimum"]["Value"])
            coldest_day = convert_date(data["Date"])
        if convert_f_to_c(data["Temperature"]["Minimum"]["Value"]) < coldest_temp:
            coldest_temp = convert_f_to_c(data["Temperature"]["Minimum"]["Value"])
            coldest_day = convert_date(data["Date"])
        if highest_temp is None:
            highest_temp = convert_f_to_c(data["Temperature"]["Maximum"]["Value"])
            highest_day = convert_date(data["Date"])
        if convert_f_to_c(data["Temperature"]["Maximum"]["Value"]) > highest_temp:
            highest_temp = convert_f_to_c(data["Temperature"]["Maximum"]["Value"])
            highest_day = convert_date(data["Date"])


    #calculating average low for 5 Day Overview
    sum_of_minimum_temps = sum(minimum_temps)
    number_minimum_temps = len(minimum_temps)
    average_low = calculate_mean((sum_of_minimum_temps), (number_minimum_temps))
    # print(average_low)

    #calculating average high for 5 Day Overview
    sum_of_maximum_temps = sum(maximum_temps)
    number_of_maximum_temps = len(maximum_temps)
    average_high = calculate_mean((sum_of_maximum_temps), (number_of_maximum_temps))
    # print(average_high)


    line = f"{len(minimum_temps)} Day Overview"
    output.append(line)
    line2 = f"    The lowest temperature will be {format_temperature(min(minimum_temps))}, and will occur on {coldest_day}."
    output.append(line2)
    line3 = f"    The highest temperature will be {format_temperature(max(maximum_temps))}, and will occur on {highest_day}."
    output.append(line3)
    line4 = f"    The average low this week is {format_temperature(average_low)}."
    output.append(line4)
    line5 = f"    The average high this week is {format_temperature(average_high)}.\n"
    output.append(line5)
   

    for x in range(len(dates)):
        dsline = f"-------- {dates[x]} --------"
        output.append(dsline)
        dsline2 = f"Minimum Temperature: {format_temperature(minimum_temps[x])}"
        output.append(dsline2)
        dsline3 = f"Maximum Temperature: {format_temperature(maximum_temps[x])}"
        output.append(dsline3)
        dsline4 = f"Daytime: {day_long_phase[x]}"
        output.append(dsline4)
        dsline5 = f"    Chance of rain:  {day_chance_rain[x]}%"
        output.append(dsline5)
        dsline6 = f"Nighttime: {night_long_phase[x]}"
        output.append(dsline6)
        dsline7 = f"    Chance of rain:  {night_chance_rain[x]}%\n"
        output.append(dsline7)

    final_output = "\n".join(output)
    final_output = final_output + "\n"
    return final_output


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_10days.json"))
    
 

 