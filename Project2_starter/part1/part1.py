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
    celsius_temperature = (float(temp_in_farenheit) - 32.0) * 5.0 / 9.0
    return celsius_temperature


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = total / num_items
    return mean


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass
    with open(forecast_file) as json_file:
       forecast_data = json.load(json_file)
  
    overall_minimum_temp = []
    overall_maximum_temp = []
    daily_summary = []
    coldest_temp = None
    coldest_day = ""
    highest_temp = None
    highest_day = ""


    for forecast in forecast_data["DailyForecasts"]:
        minimum_temp = forecast["Temperature"]["Minimum"]["Value"]
        maximum_temp = forecast["Temperature"]["Maximum"]["Value"]
        overall_minimum_temp.append(convert_f_to_c(minimum_temp))
        overall_maximum_temp.append(convert_f_to_c(maximum_temp))
        date = convert_date(forecast["Date"])
        day_long_phase = forecast["Day"]["LongPhrase"]
        day_chance_rain = forecast["Day"]["RainProbability"]
        night_long_phase = forecast["Night"]["LongPhrase"]
        night_chance_rain = forecast["Night"]["RainProbability"]
        if coldest_temp is None:
            coldest_temp = minimum_temp
            coldest_day = date
        if minimum_temp < coldest_temp:
            coldest_temp = minimum_temp
            coldest_day = date
        if highest_temp is None:
            highest_temp = maximum_temp
            highest_day = date
        if highest_temp < maximum_temp:
            highest_temp = maximum_temp
            highest_day = date





        daily_summary.append(f"{date} {minimum_temp} {maximum_temp} {day_long_phase} {day_chance_rain} {night_long_phase} {night_chance_rain}")

    #print(daily_summary)





    # # calculating average low for 5 Day Overview
    total_overall_minimum_temp = sum(overall_minimum_temp)
    number_minimum_temps = len(overall_minimum_temp)
    average_low = calculate_mean((total_overall_minimum_temp), (number_minimum_temps))
    # # print(average_low)

    # #calculating average high for 5 Day Overview
    total_overall_maximum_temp = sum(overall_maximum_temp)
    number_maximum_temps = len(overall_maximum_temp)
    average_high = calculate_mean((total_overall_maximum_temp), (number_maximum_temps))
    # print(average_high)


    print(f"""5 Day Overview \n
            The Lowest temperature will be {min(overall_minimum_temp):.1f}, and will occur on {coldest_day}. \n
            The heighest temperature will be {max(overall_maximum_temp):.1f}, and will occur on {highest_day}. \n 
            The average low this week is {(average_low):.1f}. \n 
            The average high this week is {(average_high):.1f}. \n 
    """)



if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))



with open("data/forecast_5days_a.json") as json_file:
        forecast_data = json.load(json_file)








