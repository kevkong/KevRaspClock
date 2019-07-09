from guizero import *

class VIEW(object):
    def __init__(self):
        self.setAlarm = False
        
        self.app = App(title="KevClockPi", width=480, height=320)
        self.topPanel0 = Box(self.app, width='fill', height=110)
        self.middlePanel0 = Box(self.app, width='fill', height=100)
        self.botPanel0 = Box(self.app, width='fill', height=110)

        self.box0 = Box(self.topPanel0, width=140, height='fill', align='left')
        self.box1 = Box(self.topPanel0, width='fill', height='fill', align='left')
        self.box2 = Box(self.topPanel0, width=140, height='fill',align='left')
        
        self.weatherTempText = Text(self.box1, size=25, width="fill", height="fill")
        self.weatherCondText = Text(self.box1, size=20, width="fill", height="fill")
        self.cpuTempText = Text(self.box2, size=20, width="fill", height="fill")
        self.cpuLoadText = Text(self.box2, size=20, width="fill", height="fill")

        self.box3 = Box(self.middlePanel0, width=140, height='fill', align='left')
        self.box4 = Box(self.middlePanel0, border=5, width='fill', height='fill', align='left')
        self.box5 = Box(self.middlePanel0, width=140, height='fill',align='left')

        self.dateText = Text(self.box3, text="11-Nov-2019", size=15, width="fill", height="fill")
        self.dayText = Text(self.box3, text="Sunday", size=20, width="fill", height="fill")
        self.timeText = Text(self.box4, text="11:11", size=35, width="fill", height="fill")
        self.alarmText = Text(self.box5, text="--:--", size=15, width="fill", height="fill")

        self.box6 = Box(self.botPanel0, width=140, height='fill', align='left')
        self.box7 = Box(self.botPanel0, width='fill', height='fill', align='left')
        self.box8 = Box(self.botPanel0, width=140, height='fill',align='left')

        numArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.numBox = Box(self.box7, width='fill', height=50, align='top')
        self.num1 = Combo(self.numBox, options=numArray[:3], width='fill', height='2', align='left')
        self.num2 = Combo(self.numBox, options=numArray, width='fill', height='2', align='left')
        self.num3 = Combo(self.numBox, options=numArray[:6], width='fill', height='2', align='left')
        self.num4 = Combo(self.numBox, options=numArray, width='fill', height='2', align='left')
        self.button = PushButton(self.box7, text='Set Alarm', width='fill', height='fill', command=self.saveAlarmTime)
        self.button.text_size = 15
        
    def display(self):
        self.app.display()
    
    def setColors(self):
        self.box1.bg='light blue'
        self.box3.bg='orange'
        self.box4.bg='yellow'
        self.box5.bg='orange'
        
    def updateTime(self, time):
        self.timeText.value = time
        
    def updateDateAndDay(self, date, day):
        self.dateText.value = date
        self.dayText.value = day
    
    def updateWeather(self, temp, cond):
        self.weatherTempText.value = temp
        self.weatherCondText.value = cond
        
    def updateSysInfo(self, cpuTemp, cpuLoad):
        self.cpuTempText.value = cpuTemp
        self.cpuLoadText.value = cpuLoad
            
    def saveAlarmTime(self):
        firstDigit = self.num1.value
        secondDigit = self.num2.value
        thirdDigit = self.num3.value
        forthDigit = self.num4.value
        self.alarmTime = firstDigit + secondDigit + ":" + thirdDigit + forthDigit
        self.setAlarm = True
        
    def getAlarmTime(self):
        self.setAlarm =False
        return self.alarmTime
    
    def checkIsAlarmSet(self):
        return self.setAlarm
    
    def updateAlarmTimes(self, alarms):
        self.alarmText.value = alarms