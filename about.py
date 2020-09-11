from tkinter import Tk, Label


def run():
    root = Tk()
    root.title("О программе")
    Label(root,
          text='Автор: Саидмуродов Сирожиддин\n'
               'ИВМиИТ\n'
               '09-852\n2020').pack()
    root.mainloop()
