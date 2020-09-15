from tkinter import Tk, Button
import pygame

pygame.init()
sound = r'alarm.mp3'


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

    pygame.mixer_music.load(sound)
    pygame.mixer_music.play(5)

    root.title("Будильник")
    root.mainloop()
    pygame.mixer_music.stop()


if __name__ == '__main__':
    alarm_ring_gui()
