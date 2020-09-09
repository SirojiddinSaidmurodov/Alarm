import time
import threading

import PySimpleGUIQt as sGUI
import alarm as a


def show_tray_icon():
    menu_def = ['BLANK', ['&Open', '---', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]
    tray = sGUI.SystemTray(menu=menu_def, filename=r'icon.png')
    while True:  # The event loop
        menu_item = tray.read()
        print(menu_item)
        if menu_item == 'Exit':
            break
        elif menu_item == 'Open':
            sGUI.popup('Menu item chosen', menu_item)


def main_thread(alarm: a.Alarm):
    ring_time = False
    while True:
        if alarm.is_ring_time() and not ring_time:
            ring_time = True
            pass
        else:
            ring_time = False
        time.sleep(5)


if __name__ == '__main__':
    alarm_entity = a.Alarm()
    main_loop = threading.Thread(target=main_thread, args=(alarm_entity,), daemon=True)
    show_tray_icon()
