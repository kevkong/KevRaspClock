import datetime
from datetime import datetime as dt
from weather import Weather, Unit
import requests
import time

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
    def __init__(self, time):
        print ("Setting Alarm")
        self.time = time
    
    def getAlarmTime(self):
        return self.time
            
class CLOCK(object):
    def __init__(self):
        print ("Starting Clock")
        self.dateFormat = "%d/%b/%Y"
        self.timeFormat = "%H:%M:%S"
        self.dayFormat = "%A"
        self.datetime = dt.today()
        self.date = self.datetime.strftime(self.dateFormat)
        self.time = self.datetime.strftime(self.timeFormat)
        self.day = self.datetime.strftime(self.dayFormat)
        self.RUN_CLOCK = True
        print (self.date)
        print ("Today is " + self.day)
        alarm = ALARM("00:51")
        self.alarmTime = alarm.getAlarmTime()
    
    def start(self):
        try:
            while self.RUN_CLOCK:
                timeNow =dt.today().strftime(self.timeFormat)
                print (timeNow)
                if timeNow[:-3] == self.alarmTime:
                    print ("WAKE UP NOW !!!")
                    self.RUN_CLOCK = False
                time.sleep(1)
                
        except KeyboardInterrupt:
            print ("Clock stopped")
            self.RUN_CLOCK = False    
        
def main():
    #weather = WEATHER()
    #condition = weather.getCondition()
    #temperature = weather.getTemperature()
    #print (temperature)
    clock = CLOCK()
    clock.start()
    
if __name__ == "__main__":
    main()