
# importing requests library
import requests as rq

# api_key
api_key = '30d4741c779ba94c470ca1f63045390a'

# City from user
user_input_city = input("Please enter the city \n")

# Fetch weather data from OpenWeatherMap API
weather_data = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input_city}&units=imperial&APPID={api_key}")

# Print new lines for better formatting
print("\n\n")



# Print raw JSON response
#print(weather_data.json())

if weather_data.status_code==404:

    print(f"Sorry!! City -{user_input_city} not found.")


    
else:

    # Extract weather information from JSON response

    #Extracting weather
    weather = weather_data.json()["weather"][0]["main"]

    #Extracting Temperature in farenheat
    temperature_farenheat= round(weather_data.json()["main"]["temp"])

    #Extracting Temperature in farenheat
    temperature_celsius=round((temperature_farenheat-32)*(5/9))

    #Extracting sunrise
    sunrise = weather_data.json()["sys"]["sunrise"]

    #Extracting sunrise
    sunset = weather_data.json()["sys"]["sunset"]

    # Display weather details
    print(f"Weather at {user_input_city} is : {weather}\n")

    print(f"Temperature in {user_input_city} is : {temperature_celsius}°c\n")

    print(f"Sunrise : {sunrise}\n")

    print(f"Sunset : {sunset}\n")