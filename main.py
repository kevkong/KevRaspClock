import datetime
from datetime import datetime as dt
from weather import Weather, Unit
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
        return self.data['weather']['description']
        
        
    def getCondition(self):
        condition = ""
        return condition

class ALARM(object):
    def __init__(self, date, time, day):
        self.statement = "Wake up"
        self.date = date
        self.time = time
        self.day = day
    
    def start(self):
        print (self.statement)
        print (self.date)
        print (self.time)
        print ("Today is " + self.day)
    
        
def main():
    currentDateTime = dt.today()
    dateFormat = "%d/%b/%Y"
    timeFormat = "%H:%M:%S"
    dayFormat = "%A"
    strDate = currentDateTime.strftime(dateFormat)
    strTime = currentDateTime.strftime(timeFormat)
    strDay = currentDateTime.strftime(dayFormat)
    #weather = WEATHER()
    #condition = weather.getCondition()
    #temperature = weather.getTemperature()
    #print (temperature)
    alarm = ALARM(strDate, strTime, strDay)
    alarm.start()
    
if __name__ == "__main__":
    main()