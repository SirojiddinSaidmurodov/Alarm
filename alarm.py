import time


class Alarm(object):
    def __init__(self, alarms: list):
        self.alarms = alarms

    def set(self, alarms: list):
        self.alarms = alarms

    def is_ring_time(self):
        return time.strftime('%H:%M %a') in self.alarms
