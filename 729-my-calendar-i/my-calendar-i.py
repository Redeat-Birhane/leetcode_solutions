class MyCalendar:

    def __init__(self):
        self.events = []
    def book(self, startTime: int, endTime: int) -> bool:
        self.events = sorted(self.events, key = lambda item:item[0])
        idx = bisect.bisect_left(self.events, (startTime, endTime))
        if idx > 0 and self.events[idx - 1][1] > startTime:
            return False
        if idx < len(self.events) and self.events[idx][0] < endTime:
            return False
        self.events.append((startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)