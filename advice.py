import requests

class ADVICE(object):
    def __init__(self):
        self.getAdviceData()
        
    def getAdviceData(self):
        url = "https://api.adviceslip.com/advice"
        self.adviceData = requests.get(url).json()
    
    def getAdvice(self):
        return self.adviceData['slip']['advice']