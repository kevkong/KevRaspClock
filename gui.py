from guizero import *
app = App(title="KevClockPi", width=480, height=320)
topPanel0 = Box(app, width='fill', height=110)
middlePanel0 = Box(app, width='fill', height=100)
botPanel0 = Box(app, width='fill', height=110)

box0 = Box(topPanel0, width=140, height='fill', align='left')
box1 = Box(topPanel0, width='fill', height='fill', align='left')
box2 = Box(topPanel0, width=140, height='fill',align='left')

box3 = Box(middlePanel0, width=140, height='fill', align='left')
box4 = Box(middlePanel0, border=5, width='fill', height='fill', align='left')
box5 = Box(middlePanel0, width=140, height='fill',align='left')

dateText = Text(box3, text="11 APRIL 2019", size=10, width="fill", height="fill")
timeText = Text(box4, text="11:00", size=45, width="fill", height="fill")

box3.bg='orange'
box4.bg='yellow'
box5.bg='orange'

box6 = Box(botPanel0, width=140, height='fill', align='left')
box7 = Box(botPanel0, width='fill', height='fill', align='left')
box8 = Box(botPanel0, width=140, height='fill',align='left')

numArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numBox = Box(box7, width='fill', height=50, align='top')
num1 = Combo(numBox, options=numArray, width='fill', height='2', align='left')
num2 = Combo(numBox, options=numArray, width='fill', height='2', align='left')
num3 = Combo(numBox, options=numArray, width='fill', height='2', align='left')
num4 = Combo(numBox, options=numArray, width='fill', height='2', align='left')
button = PushButton(box7, text='Set Alarm', width='fill', height='fill')
button.text_size = 15

app.display()