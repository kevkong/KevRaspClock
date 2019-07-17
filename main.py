#!/usr/bin/env python3

import time
import os
import re
from weather import WEATHER
from alarm import ALARM
from utils import ThreadHandler
from clock import CLOCK
from controller import CONTROLLER
from advice import ADVICE

def main():
    #weather = WEATHER()
    #condition = weather.getCondition()
    #temperature = weather.getTemperature()
    #print (temperature)
    
    weather = WEATHER()
    myAlarms = []
    clock = CLOCK(myAlarms)
    advice = ADVICE()
#    allInput = ALLINPUT(clock, myAlarms, weather)
    
    controller = CONTROLLER(clock, myAlarms, weather, advice)
    controller.startDisplayView()
    
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