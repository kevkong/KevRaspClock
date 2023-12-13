import psutil

print(psutil.sensors_temperatures())

class SYSSTATUS(object):
    def getCpuTemp(self):
        temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
        return str(round(temp,1)) + " " + chr(176) + "C"
    
    def getCpuLoad(self):
        return str(psutil.cpu_percent()) + " " + chr(37)