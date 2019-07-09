import requests

class WEATHER(object):
    def __init__(self):
        self.units = "metric"
        self.apiKey = "f5f8c7b035b03661155a5da193520eda"
        self.cityID = "1735106"
        self.fetchWeatherData()

    def fetchWeatherData(self):
        url = "https://api.openweathermap.org/data/2.5/weather?id={}&units={}&appid={}".format(self.cityID, self.units, self.apiKey)
        self.data = requests.get(url).json()

    def getTemperature(self):
        return self.data['main']['temp']

    def getTempMin(self):
        return self.data['main']['temp_min']

    def getTempMax(self):
        return self.data['main']['temp_max']

    def getHumidity(self):
        return self.data['main']['humidity']

    def getCondition(self):
        #can fetch picture from openweather and use
        return self.data['weather'][0]['description']