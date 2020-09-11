import time as t


class AlarmContainer(object):
    def __init__(self, alarms=None):
        if alarms is None:
            alarms = []
        self.alarms = alarms

    def set_alarms(self, alarms: list):
        self.alarms = alarms

    def is_ring_time(self):
        return Alarm() in self.alarms


class Alarm(object):
    def __init__(self, time=t.strftime('%H:%M'), weekdays=2 ** int(t.strftime('%w'))):
        self.weekdays = weekdays
        self.time = time

    def __str__(self):
        result = self.time
        result += "  "
        result += str(bin(self.weekdays))
        return result

    def __eq__(self, other):
        if self.time == other.time:
            if self.weekdays & other.weekdays:
                return True
        return False
