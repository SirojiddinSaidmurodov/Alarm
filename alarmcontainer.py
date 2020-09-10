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


def format_days(week_day):
    result_list = []
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", " Sunday"]:
        if day in week_day:
            result_list.append(day)
        else:
            result_list.append("")
    return result_list


class Alarm(object):
    def __init__(self, time=t.strftime('%H:%M'), week_days=None):
        if week_days is None:
            self.weekdays = t.strftime('%a')
        else:
            self.weekdays = format_days(week_days)
        self.time = time

    def __eq__(self, other):
        if self.time == other.time:
            if self.weekdays in other.weekdays:
                return True
        return False


if __name__ == '__main__':
    alarm = AlarmContainer([Alarm('03:41', 'Thursday')])
    while True:
        if alarm.is_ring_time():
            print("Ala")
        else:
            print("not yet")
        t.sleep(2)
