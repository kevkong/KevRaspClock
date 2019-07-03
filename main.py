import datetime
from datetime import datetime as dt
import time
import os
import threading
import re

class ThreadHandler():
    STEP = 0.2

    def __init__(self, target):
        self.lock = threading.Lock()
        self.stop = threading.Event()
        args = (self.lock, self.stop)
        self.thread = threading.Thread(target=target, args=args)

    def start(self):
        self.thread.start()

    def setStop(self):
        self.stop.set()

    def join(self):
        while self.thread.is_alive():
            try:
                self.thread.join()
            except KeyboardInterrupt:
                self.stop.set()

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


class ALARM(object):
    def __init__(self, end):
        print ("Setting Alarm")
        self.endTime = end
        self.switch = True

    def getEndTime(self):
        return self.endTime

    def getSwitch(self):
        return self.switch

    def turnOff(self):
        self.switch = False

class CLOCK(object):
    def __init__(self, alarms):
        print ("Starting Clock")
        self.dateFormat = "%d/%b/%Y"
        self.timeFormat = "%H:%M:%S"
        self.dayFormat = "%A"
        self.datetime = dt.today()
        self.date = self.datetime.strftime(self.dateFormat)
        self.time = self.datetime.strftime(self.timeFormat)
        self.day = self.datetime.strftime(self.dayFormat)
        self.RUN_CLOCK = True
        self.alarms = alarms
        print (self.date)
        print ("Today is " + self.day)

    def start_clock_loop(self, lock, stop):
        with lock:
            print ("Clock loop started")
            time.sleep(1)
        while not stop.is_set():
            self.time =dt.today().strftime(self.timeFormat)
            if not len(self.alarms) == 0:
#                with lock:
#                    print("I have alarms")
#                    print(len(self.alarms))
                for alarm in self.alarms:
                    if self.time[:-3] == alarm.getEndTime() and alarm.getSwitch():
                        with lock:
                            print ("WAKE UP NOW !!!")
                        alarm.turnOff()
                        os.system("omxplayer -o local --loop Sounds/example.mp3 &")
                        time.sleep(5)
                        os.system("killall omxplayer.bin")
            time.sleep(1)
            #with lock:
            #    print (timeNow)
    def get_current_time(self):
        return self.time

class ALLINPUT(object):
    def __init__(self, clock, alarms):
        print("Initialize listener")
        self.input = ""
        self.clock = clock
        self.alarms = alarms

    def userInputListener(self, lock, stop):
        while not stop.is_set():
            with lock:
                print ("Enter input:")
            self.input = input()
            self.processInput(lock)

    def processInput(self, lock):
        matchSetGetTime = re.match(r'time', self.input)
        matchSetAlarm = re.match(r'alarm\s(\d+:\d+)', self.input)
        matchSetDeleteAlarm = re.match(r'delete alarm', self.input)

        if matchSetGetTime:
            with lock:
                print (self.clock.get_current_time())

        if matchSetAlarm:
            newAlarm = ALARM(matchSetAlarm.group(1))
            with lock:
                print ("Adding Alarm")
            self.alarms.append(newAlarm)

        if matchSetDeleteAlarm:
            with lock:
                print ("Deleting Alarm")
            self.alarms.pop()

    def getInput(self):
        return self.input

def main():
    #weather = WEATHER()
    #condition = weather.getCondition()
    #temperature = weather.getTemperature()
    #print (temperature)
    weather = WEATHER()
    temperature = weather.getTemperature()
    print(temperature)
    myAlarms = []
    clock = CLOCK(myAlarms)
    allInput = ALLINPUT(clock, myAlarms)
    #clock.start()
    clockHandler = ThreadHandler(target=clock.start_clock_loop)
    inputHandler = ThreadHandler(target=allInput.userInputListener)
    clockHandler.start()
    time.sleep(1)
    inputHandler.start()
    clockHandler.join()
    inputHandler.join()

if __name__ == "__main__":
    main()