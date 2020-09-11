import logging
import time
import threading

import PySimpleGUIQt as sGUI

import about
import alarmcontainer as a
import settings


def show_tray_icon(alarms):
    menu_def = ['', ['&Настройки', '&О программе', '&Выход']]
    tray = sGUI.SystemTray(menu=menu_def, filename=r'icon.png')
    while True:  # The event loop
        menu_item = tray.read()
        print(menu_item)
        if menu_item == 'Выход':
            break
        elif menu_item == 'Настройки':
            logging.info("Настройки")
            settings.run(alarms)
        elif menu_item == "О программе":
            logging.info("О программе")
            about.run()


def alarm_daemon(alarm: a.AlarmContainer):
    logging.info("Running daemon")
    ring_time = False
    while True:
        if alarm.is_ring_time():
            if not ring_time:
                ring_time = True
                logging.info("Alarm is ringing")
        else:
            ring_time = False
        logging.info(alarm)
        time.sleep(5)


if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                        datefmt="%H:%M:%S")

    alarm_entity = a.AlarmContainer()
    main_loop = threading.Thread(target=alarm_daemon, args=(alarm_entity,), daemon=True)
    main_loop.start()

    show_tray_icon(alarm_entity)  # endless loop
