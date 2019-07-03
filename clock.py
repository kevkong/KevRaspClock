from datetime import datetime as dt
import time

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