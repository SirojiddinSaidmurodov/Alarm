from tkinter import *
import alarmcontainer

week_days = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]


def is_valid(input_string: str):
    return input_string.isdigit() and 59 >= int(input_string) >= 0


def create_week_days_selector(container):
    f_days = LabelFrame(container, text="Дни недели")
    f_days.pack(ipadx=5, ipady=5, padx=5, pady=5)
    check_box = []
    week_sel = []
    for num, day in enumerate(week_days):
        week_sel.append(IntVar())
        check_box.append(
            Checkbutton(f_days, text=day, variable=week_sel[num], onvalue=1, offvalue=0, indicatoron=0))
        check_box[num].pack(side=LEFT, padx=5, pady=5)
    return week_sel


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
    return hour_entry, minute_entry


def add_zero(num):
    if len(num) < 2:
        num = "0" + num
    return num


def click_action(week, hour, minute, alarms_container: alarmcontainer.AlarmContainer):
    week_code = 0
    for num, day in enumerate(week):
        if day.get():
            week_code += 2 ** ((num + 1) % 7)
    hour = add_zero(hour.get())
    minute = add_zero(minute.get())
    time = hour + ":" + minute
    alarms_container.add_alarm(alarmcontainer.Alarm(time, week_code))


def create_done_button(week, hour, minute, container):
    btn = Button(text="Добавить будильник", background="#555", foreground="#ccc",
                 padx="20", pady="8", font="16", command=lambda: click_action(week, hour, minute, container))
    btn.pack()


def run(alarms_container):
    root = Tk()
    root.title("Настройки будильника")
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.png'))
    week_list = create_week_days_selector(root)
    hour_spinbox, minute_spinbox = create_time_selector(root)
    create_done_button(week_list, hour_spinbox, minute_spinbox, alarms_container)
    root.mainloop()
