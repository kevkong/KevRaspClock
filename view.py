from guizero import *

class VIEW(object):
    def __init__(self):
        self.app = App(title="KevClockPi", width=480, height=320)
        self.topPanel0 = Box(self.app, width='fill', height=110)
        self.middlePanel0 = Box(self.app, width='fill', height=100)
        self.botPanel0 = Box(self.app, width='fill', height=110)

        self.box0 = Box(self.topPanel0, width=140, height='fill', align='left')
        self.box1 = Box(self.topPanel0, width='fill', height='fill', align='left')
        self.box2 = Box(self.topPanel0, width=140, height='fill',align='left')

        self.box3 = Box(self.middlePanel0, width=140, height='fill', align='left')
        self.box4 = Box(self.middlePanel0, border=5, width='fill', height='fill', align='left')
        self.box5 = Box(self.middlePanel0, width=140, height='fill',align='left')

        self.dateText = Text(self.box3, text="11-Nov-2019", size=15, width="fill", height="fill")
        self.timeText = Text(self.box4, text="11:11", size=40, width="fill", height="fill")

        self.box3.bg='orange'
        self.box4.bg='yellow'
        self.box5.bg='orange'

        self.box6 = Box(self.botPanel0, width=140, height='fill', align='left')
        self.box7 = Box(self.botPanel0, width='fill', height='fill', align='left')
        self.box8 = Box(self.botPanel0, width=140, height='fill',align='left')

        numArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.numBox = Box(self.box7, width='fill', height=50, align='top')
        self.num1 = Combo(self.numBox, options=numArray, width='fill', height='2', align='left')
        self.num2 = Combo(self.numBox, options=numArray, width='fill', height='2', align='left')
        self.num3 = Combo(self.numBox, options=numArray, width='fill', height='2', align='left')
        self.num4 = Combo(self.numBox, options=numArray, width='fill', height='2', align='left')
        self.button = PushButton(self.box7, text='Set Alarm', width='fill', height='fill')
        self.button.text_size = 15