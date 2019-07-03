from view import VIEW

class CONTROLLER(object):
    def __init__(self, clock):
        print("Setup view")
        self.view = VIEW()
        print("Setup clock")
        self.clock = clock
        print("Setup bindings")
        self.binding()
        self.startTimeAndDate()
        
    def binding(self):
        self.view.app.repeat(1000, self.updateTimeAndDate)
        
    def displayView(self):
        self.view.app.display()
    
    def startTimeAndDate(self):
        self.view.timeText.value = self.clock.getCurrentTime()
        self.view.dateText.value = self.clock.getCurrentDate()

    def updateTimeAndDate(self):
        time = self.clock.getCurrentTime()
        self.view.timeText.value = time
        if (time == "00:00:00"):
            self.view.dateText.value = self.clock.getCurrentDate()