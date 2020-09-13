import threading
import time
from tkinter import Tk, Button, PhotoImage

import playsound

sound = r'alarm.mp3'


def make_sound(event: threading.Event):
    time.sleep(5)
    while not event.is_set():
        playsound.playsound(sound)


def alarm_ring_gui():
    root = Tk()
    btn = Button(text="Выключить будильник",
                 background="#f00",
                 foreground="#000",
                 activebackground='#00f',
                 activeforeground='#fff',
                 padx="20",
                 pady="20",
                 font="Arial 72",
                 command=root.destroy)
    btn.pack()
    stop_event = threading.Event()
    daemon = threading.Thread(target=make_sound, daemon=True, args=(stop_event,))
    daemon.start()
    root.title("Будильник")
    root.mainloop()
    stop_event.set()
