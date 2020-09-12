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

    def add_alarm(self, alarm):
        self.alarms.append(alarm)

    def __str__(self):
        result = ''
        for a in self.alarms:
            result += str(a) + '\n'
        return result


class Alarm(object):
    def __init__(self, time=None, weekdays=None):
        if time is None:
            time = t.strftime('%H:%M')
        if weekdays is None:
            weekdays = 2 ** int(t.strftime('%w'))
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
