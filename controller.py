from view import VIEW
from alarm import ALARM
from sysstatus import SYSSTATUS

class CONTROLLER(object):
    def __init__(self, clock, alarms, weather, advice, pihole):
        print("Setup view")
        self.view = VIEW(alarms)
        print("Setup clock")
        self.clock = clock
        self.alarms = alarms
        self.weather = weather
        self.advice = advice
        self.sysStat = SYSSTATUS()
        self.pihole = pihole
        print("Setup bindings")
        self.binding()
        
    def binding(self):
        self.view.app.repeat(1000, self.tickTock)
        
    def tickTock(self):
        time= self.clock.getCurrentTime()
        self.updateView(time)
        self.checkAlarmInput()
        self.checkAlarmActive(time)
        
    def startDisplayView(self):
        time= self.clock.getCurrentTime()
        date = self.clock.getCurrentDate()
        day = self.clock.getCurrentDay()
        weatherTemp = str(self.weather.getTemperature()) + " " + chr(176) + "C"
        weatherCond = self.weather.getCondition()
        self.view.updateSysInfo(self.sysStat.getCpuTemp(), self.sysStat.getCpuLoad())
        self.view.updateTime(time)
        self.view.updateDateAndDay(date, day)
        self.view.updateWeather(weatherTemp, weatherCond)
        self.view.updateAdvice(self.advice.getAdvice())
        self.view.updatePiHole(self.getPiHoleDict())
        self.view.setColors()
        self.view.display()

    def updateView(self, time):
        self.view.updateTime(time)
        self.view.updateSysInfo(self.sysStat.getCpuTemp(), self.sysStat.getCpuLoad())
        self.pihole.refresh()
        self.view.updatePiHole(self.getPiHoleDict())
        if (time[:-2] == "00"):
            weatherTemp = str(self.weather.getTemperature()) + " " + chr(176) + "C"
            weatherCond = self.weather.getCondition()
            self.view.updateWeather(weatherTemp, weatherCond)
            self.view.updateAdvice(self.advice.getAdvice())
            
        if (time == "00:00:00"):
            date = self.clock.getCurrentDate()
            day = self.clock.getCurrentDay()
            self.view.updateDateAndDay(date, day)
    
    def checkAlarmInput(self):
        if (self.view.checkIsAlarmSet()):
            newAlarm = ALARM(self.view.getAlarmTime())
            self.alarms.append(newAlarm)
            self.view.createAlarmText(self.view.getAlarmTime())
#        if (len(self.alarms) > 0):
#            self.view.updateAlarmTimes(self.getAlarmsStr())
#        else:
#            self.view.updateAlarmTimes("--:--")
            
    def getAlarmsStr(self):
        tmpStr = ""
        for alarm in self.alarms:
            tmpStr += alarm.getEndTime() + "\n"
        return tmpStr
    
    def checkAlarmActive(self, time):
        for alarm in self.alarms:
            if time[:-3] == alarm.getEndTime() and alarm.getSwitch():
                alarm.wakeSound()
                alarm.turnOff()
                self.alarms.remove(alarm)
    
    def getPiHoleDict(self):
        return {"Status":self.pihole.status, "Queries":self.pihole.queries,
                "Blocked":self.pihole.blocked, "Percentage":self.pihole.ads_percentage}
                