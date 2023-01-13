import json

with open('data/config.json') as file:
    config = json.load(file)

isWeatherGoodToday = config['WeatherConditions']['isWeatherGoodToday']
if(isWeatherGoodToday):
    print("The weather is good today!")
else:
    print("The weather is bad today!")

