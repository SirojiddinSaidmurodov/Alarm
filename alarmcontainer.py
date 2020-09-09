import time as t


class AlarmContainer(object):
    def __init__(self, alarms=None):
        if alarms is None:
            alarms = []
        self.alarms = alarms

    def set_alarms(self, alarms: list):
        self.alarms = alarms

    def is_ring_time(self):
        return t.strftime('%H:%M %a') in self.alarms


if __name__ == '__main__':
    alarm = AlarmContainer(['10:26 Wed'])
    while True:
        if alarm.is_ring_time():
            print("Ala")
        else:
            print("not yet")
        t.sleep(2)
