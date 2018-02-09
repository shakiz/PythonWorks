import requests
api_address="https://api.openweathermap.org/data/2.5/weather?appid=c87050bbe4837a49ada52f7197118520&q="

#taking input 
print("Enter your city :")
city=raw_input()

#concating the url and city name
url=api_address+city

#sending the url through requests module
json_data=requests.get(url).json()

#gathering all reports
name=json_data['weather'][0]['main']
maxTemp=json_data['main']['temp_max']
minTemp=json_data['main']['temp_min']
currentTemp=json_data['main']['temp']
windSpeed=json_data['wind']['speed']
windDeg=json_data['wind']['deg']
des=json_data['weather'][0]['description']
hum=json_data['main']['humidity']
countryName=json_data['name']
clouds=json_data['clouds']['all']

#printing all report
print("Weather status is : ",name)
print("Description : ",des)
print("Humidity : ",hum)
print("Country : ",countryName)
print("Clouds density : ",clouds)
print("Current temperature is : ",currentTemp)
print("Maximum temperature : ",maxTemp)
print("Minimum temperature : ",minTemp)
print("Wind speed : ",windSpeed)
print("Wind degree : ",windDeg)
