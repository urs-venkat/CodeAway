# importing requests library

import requests as rq

#api_key

api_key='30d4741c779ba94c470ca1f63045390a'


#City from user 

user_input_city=input("Please enter the city \n")

weather_data= rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input_city}&units=imperial&APPID={api_key}")

print(weather_data.status_code)
