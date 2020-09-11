from tkinter import *

week_days = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]


def is_valid(input_string: str):
    return input_string.isdigit() and len(input_string) < 3


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

    time_font = 'Arial 30'
    hour_entry = Spinbox(f_time, width=4, from_=0, to=23, wrap=True, font=time_font)
    minute_entry = Spinbox(f_time, width=4, from_=0, to=59, wrap=True, font=time_font)
    hour_entry.pack(side=LEFT)
    Label(f_time, text=':', font=time_font).pack(side=LEFT)
    minute_entry.pack(side=LEFT)

    reg = container.register(is_valid)
    hour_entry.config(validate='key', validatecommand=(reg, '%P'))
    minute_entry.config(validate='key', validatecommand=(reg, '%P'))


def run():
    root = Tk()
    root.title("Настройки будильника")
    create_week_days_selector(root)
    create_time_selector(root)
    root.mainloop()


if __name__ == "__main__":
    run()
