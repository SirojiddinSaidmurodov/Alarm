import logging
import time
import threading
from tkinter import Tk

import PySimpleGUIQt as sGUI
import alarm as a


def show_tray_icon():
    menu_def = ['', ['&Настройки', '&Выход']]
    tray = sGUI.SystemTray(menu=menu_def, filename=r'icon.png')
    while True:  # The event loop
        menu_item = tray.read()
        print(menu_item)
        if menu_item == 'Выход':
            break
        elif menu_item == 'Настройки':
            logging.info("Settings menu event")


def main_thread(alarm: a.Alarm):
    logging.info("Running daemon")
    ring_time = False
    while True:
        if alarm.is_ring_time():
            if not ring_time:
                ring_time = True
                logging.info("Alarm is ringing")
        else:
            ring_time = False
        time.sleep(5)


if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                        datefmt="%H:%M:%S")

    alarm_entity = a.Alarm()
    main_loop = threading.Thread(target=main_thread, args=(alarm_entity,), daemon=True)
    main_loop.start()

    show_tray_icon()  # endless loop
