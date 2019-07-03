import time
import os
import re
from weather import WEATHER
from alarm import ALARM
from utils import ThreadHandler
from clock import CLOCK
from controller import CONTROLLER

class ALLINPUT(object):
    def __init__(self, clock, alarms, weather):
        print("Initialize listener")
        self.input = ""
        self.clock = clock
        self.alarms = alarms
        self.weather = weather

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
        matchGetTemp = re.match(r'temp', self.input)

        if matchSetGetTime:
            with lock:
                print (self.clock.getCurrentTime())

        if matchSetAlarm:
            newAlarm = ALARM(matchSetAlarm.group(1))
            with lock:
                print ("Adding Alarm")
            self.alarms.append(newAlarm)

        if matchSetDeleteAlarm:
            with lock:
                print ("Deleting Alarm")
            self.alarms.pop()
            
        if matchGetTemp:
            with lock:
                print (self.weather.getTemperature())
            

    def getInput(self):
        return self.input

def main():
    #weather = WEATHER()
    #condition = weather.getCondition()
    #temperature = weather.getTemperature()
    #print (temperature)
    
    weather = WEATHER()
    myAlarms = []
    clock = CLOCK(myAlarms)
#    allInput = ALLINPUT(clock, myAlarms, weather)
    
    controller = CONTROLLER(clock)
    controller.displayView()
    
#    clockHandler = ThreadHandler(target=clock.start_clock_loop)
#    inputHandler = ThreadHandler(target=allInput.userInputListener)
#    controllerHandler = ThreadHandler(target=controller.displayView)
#    clockHandler.start()
#    controllerHandler.start()
#    time.sleep(1)
#    inputHandler.start()
#    clockHandler.join()
#    inputHandler.join()

if __name__ == "__main__":
    main()