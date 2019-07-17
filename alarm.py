import os

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
        print ("Turn off Alarm")
        self.switch = False
        
    def wakeSound(self):
        os.system("omxplayer -o local /home/pi/KevRaspClock/Sounds/example.mp3 &")
#        os.system("omxplayer -o local --loop Sounds/example.mp3 &")
#        time.sleep(5)
#        os.system("killall omxplayer.bin")
