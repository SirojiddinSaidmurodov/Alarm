from tkinter import *

week_days = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]


def create_week_days_selector(container):
    f_days = LabelFrame(container, text="Дни недели")
    f_days.pack(ipadx=5, ipady=5, padx=5, pady=5)
    check_box = []
    week_sel = []
    for num, day in enumerate(week_days):
        week_sel.append(BooleanVar())
        check_box.append(
            Checkbutton(f_days, text=day, variable=week_sel[num], onvalue=1, offvalue=0, indicatoron=0))
        check_box[num].pack(side=LEFT, padx=5, pady=5)


def create_time_selector(container):
    f_time = LabelFrame(container, text="Время")
    f_time.pack()
    hour = StringVar()
    minute = StringVar()
    hour_entry = Entry(f_time, textvariable=hour, width=2)
    minute_entry = Entry(f_time, textvariable=minute, width=2)
    hour_entry.insert(0, "00")
    minute_entry.insert(0, "00")
    hour_entry.pack()
    minute_entry.pack()


def run():
    root = Tk()
    root.title("Настройки будильника")
    create_week_days_selector(root)
    create_time_selector(root)
    root.mainloop()


if __name__ == "__main__":
    run()
