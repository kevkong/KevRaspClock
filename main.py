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
# import pihole as ph

def main():
    
    # pihole = ph.PiHole("192.168.100.49")
#    print(pihole.status, pihole.domain_count, pihole.queries, pihole.blocked, pihole.ads_percentage,
#pihole.unique_domains, pihole.forwarded, pihole.cached, pihole.total_clients, pihole.unique_clients,
#pihole.total_queries)
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