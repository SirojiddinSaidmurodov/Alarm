from tkinter import *


def run():
    root = Tk()
    root.title("Настройки будильника")
    value = StringVar(root)
    value.set("Monday")  # default value
    options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", " Sunday"]
    week_selector = OptionMenu(root, value, *options)
    week_selector.pack()
    root.mainloop()


if __name__ == "__main__":
    run()
