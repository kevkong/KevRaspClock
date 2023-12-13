from guizero import *

class VIEW(object):
    def __init__(self, alarms):
        print(system_config.supported_image_types)
        self.appWidth = 480
        self.appHeight = 320
        self.fullWidth = self.appWidth
        self.fullHeight = self.appHeight
        self.sfW = 1
        self.sfH = 1
        self.dummy = App()
        self.dummy.full_screen = True
        self.dummy.after(300, self.dummyCommand)
        self.dummy.display()
        self.setAlarm = False
        self.alarmTexts = []
        self.alarms = alarms
        self.alarmHour = 0
        self.alarmMinute = 0
        self.sidePanelH = self.dividedH-round(self.dividedH/10)
        self.sideBoxW = 2*self.dividedW
        self.midPanelH = self.fullHeight-2*self.sidePanelH
        self.timeTS = round(35*self.sfH)
        self.otherTS = round(20*self.sfH)
        
        self.app = App(title="KevClockPi", width=self.appWidth, height=self.appHeight)
        self.app.full_screen = True
        self.topPanel0 = Box(self.app, width='fill', height=self.sidePanelH)
        self.middlePanel0 = Box(self.app, width='fill', height=self.midPanelH)
        self.botPanel0 = Box(self.app, width='fill', height=self.sidePanelH)

        self.box0 = Box(self.topPanel0, width=self.sideBoxW, height='fill', align='left')
        self.box1 = Box(self.topPanel0, width='fill', height='fill', align='left')
        self.box2 = Box(self.topPanel0, width=self.sideBoxW, height='fill',align='left')
        
        self.exitButton = PushButton(self.box0, command=self.app.destroy, image = "/home/pi/KevRaspClock/Images/3rddrawing.gif")
        
        self.weatherTempText = Text(self.box1, size=self.otherTS , width="fill", height="fill")
        self.weatherCondText = Text(self.box1, size=self.otherTS , width="fill", height="fill")
        self.cpuTempText = Text(self.box2, size=self.otherTS , width="fill", height="fill")
        self.cpuLoadText = Text(self.box2, size=self.otherTS , width="fill", height="fill")

        self.box3 = Box(self.middlePanel0, width=self.sideBoxW, height='fill', align='left')
        self.box4 = Box(self.middlePanel0, border=5, width='fill', height='fill', align='left')
        self.box5 = Box(self.middlePanel0, width=self.sideBoxW, height='fill',align='left')

        self.dateText = Text(self.box3, text="11-Nov-2019", size=round(self.otherTS*3/4) , width="fill", height="fill")
        self.dayText = Text(self.box3, text="Sunday", size=self.otherTS , width="fill", height="fill")
        self.timeText = Text(self.box4, text="11:11", size=self.timeTS, width="fill", height="fill")
        
        self.alarmViewBox = Box(self.box5)
        self.alarmButtonSize = round(self.otherTS*3/2)
        self.addAlarmButton = PushButton(self.alarmViewBox, align='right', width=self.alarmButtonSize, height=self.alarmButtonSize, command=self.addAlarm, image = "/home/pi/KevRaspClock/Images/baseline_add_black_18dp.png")

        self.alarmSetBox = Box(self.box5, layout='grid', visible=False)
        buttonWidth = self.alarmButtonSize
        buttonHeight = self.alarmButtonSize
        self.hourUpButton = PushButton(self.alarmSetBox, grid=[0,0,2,1], width=buttonWidth, height=buttonHeight, command=self.upAlarmHour, image = "/home/pi/KevRaspClock/Images/baseline_arrow_drop_up_black_18dp.png")
        self.hourDownButton = PushButton(self.alarmSetBox, grid=[0,3,2,1], width=buttonWidth, height=buttonHeight, command=self.downAlarmHour, image = "/home/pi/KevRaspClock/Images/baseline_arrow_drop_down_black_18dp.png")
        self.minuteUpButton = PushButton(self.alarmSetBox, grid=[3,0,2,1], width=buttonWidth, height=buttonHeight, command=self.upAlarmMinute, image = "/home/pi/KevRaspClock/Images/baseline_arrow_drop_up_black_18dp.png")
        self.minuteDownButton = PushButton(self.alarmSetBox, grid=[3,3,2,1], width=buttonWidth, height=buttonHeight, command=self.downAlarmMinute, image = "/home/pi/KevRaspClock/Images/baseline_arrow_drop_down_black_18dp.png")
        alarmSetTextSize = self.alarmButtonSize
        self.hourText = Text(self.alarmSetBox, text="00", size=alarmSetTextSize, grid=[0,1,2,2])
        self.minuteText = Text(self.alarmSetBox, text="00", size=alarmSetTextSize, grid=[3,1,2,2])
        self.seperatorText = Text(self.alarmSetBox, text=':', size=alarmSetTextSize, grid=[2,1,1,2,])
        self.setAlarmButton = PushButton(self.alarmSetBox, text='Set Alarm', command=self.saveAlarmTime, grid=[0,4,5,1])
        self.setAlarmButton.text_size = round(alarmSetTextSize/2)
 
        self.box6 = Box(self.botPanel0, width=self.sideBoxW, height='fill', align='left')
        self.box7 = Box(self.botPanel0, width='fill', height='fill', align='left')
        self.box8 = Box(self.botPanel0, width=self.sideBoxW, height='fill', align='right')
        
        self.exitFullButton = PushButton(self.box6, text="", width="fill", height="fill", command=self.app.exit_full_screen)
        
        self.adviceText = Text(self.box7, size=round(self.otherTS*3/4))
        self.adviceText.tk.config(wraplength=175*self.sfW)
        # self.piHoleText = Text(self.box8, size=round(self.otherTS*5/9))
    
    def dummyCommand(self):
        self.sfW = round(self.dummy.width/self.appWidth)
        self.sfH = round(self.dummy.height/self.appHeight)
        self.fullWidth = self.dummy.width
        self.fullHeight = self.dummy.height
        self.dividedW = round(self.dummy.width/7)
        self.dividedH = round(self.dummy.height/3)
        self.dummy.destroy()
        
    def display(self):
        self.app.display()
    
    def setColors(self):
        self.box1.bg='light blue'
        self.box3.bg='orange'
        self.box4.bg='yellow'
        self.box5.bg='orange'
        self.box7.bg='light green'
        
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
        self.alarmTime = self.hourText.value + ":" + self.minuteText.value
        self.setAlarm = True
        self.alarmViewBox.visible=True
        self.alarmSetBox.visible=False
        
    def addAlarm(self):
        self.alarmViewBox.visible=False
        self.alarmSetBox.visible=True
        
    def getAlarmTime(self):
        self.setAlarm =False
        return self.alarmTime
    
    def checkIsAlarmSet(self):
        return self.setAlarm
    
#    def updateAlarmTimes(self, alarms):
#        self.alarmText.value = alarms
        
    def createAlarmText(self, alarmText):
        newText = Text(self.alarmViewBox, text=alarmText, size=self.alarmButtonSize)
        newText.when_clicked = self.alarmClickEvent
        self.alarmTexts.append(newText)
        
    def alarmClickEvent(self, event_data):
        alarm_index = self.alarmTexts.index(event_data.widget)
        self.alarmTexts.pop(alarm_index)
        self.alarms[alarm_index].turnOff()
        self.alarms.pop(alarm_index)
        event_data.widget.destroy()
    
    def upAlarmHour(self):
        self.alarmHour += 1
        if(self.alarmHour>23):
            self.alarmHour=0
        self.hourText.value = str(self.alarmHour).rjust(2, '0')
        
    def downAlarmHour(self):
        self.alarmHour -= 1
        if(self.alarmHour<0):
            self.alarmHour=23
        self.hourText.value = str(self.alarmHour).rjust(2, '0')
        
    def upAlarmMinute(self):
        self.alarmMinute += 1
        if(self.alarmMinute>59):
            self.alarmMinute=0
        self.minuteText.value = str(self.alarmMinute).rjust(2, '0')
        
    def downAlarmMinute(self):
        self.alarmMinute -= 1
        if(self.alarmMinute<0):
            self.alarmMinute=59
        self.minuteText.value = str(self.alarmMinute).rjust(2, '0')
        
    def updateAdvice(self, advice):
        self.adviceText.value = advice

    # def updatePiHole(self, piHoleDict):
    #     self.piHoleText.value = "Pi-Hole\n"
    #     for tag, piHoleInfo in piHoleDict.items():
    #         self.piHoleText.value += tag + ": " + piHoleInfo + "\n"
            