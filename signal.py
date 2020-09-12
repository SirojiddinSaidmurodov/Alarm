import threading
import time
from tkinter import Tk, Button, PhotoImage

import playsound


def make_sound():
    time.sleep(5)
    while True:
        playsound.playsound(r'alarm.mp3')


def alarm_ring_gui():
    root = Tk()
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.png'))
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
    daemon = threading.Thread(target=make_sound, daemon=True)
    daemon.start()
    root.title("Будильник")
    root.mainloop()
