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