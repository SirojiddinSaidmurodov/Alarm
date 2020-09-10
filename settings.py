from tkinter import *

week_days = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]


def weeks_selector_create(container):
    f_left = LabelFrame(container, text="Дни недели")
    f_left.pack()
    check_box = []
    week_sel = []
    for num, day in enumerate(week_days):
        week_sel.append(BooleanVar())
        check_box.append(
            Checkbutton(f_left, text=day, variable=week_sel[num], onvalue=1, offvalue=0, indicatoron=0))
        check_box[num].pack(side=LEFT)


def run():
    root = Tk()
    root.title("Настройки будильника")
    weeks_selector_create(root)
    root.mainloop()


if __name__ == "__main__":
    run()
