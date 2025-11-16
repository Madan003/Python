import datetime
class WaitingTime:
    def __init__(self, length=0, serving_time=0):
        self.queueLength = length
        self.servingTime = serving_time

    def calculateWaitingTime(self):
        minutes = self.queueLength * self.servingTime
        print(minutes)
        time = str(datetime.timedelta(minutes=minutes))
        print(f"Waitning Time is: {time}")
    
w1 = WaitingTime(4,2.4)
w1.calculateWaitingTime()