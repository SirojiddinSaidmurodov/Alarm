import PySimpleGUIQt as sg


def show_tray_icon():
    menu_def = ['BLANK', ['&Open', '---', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]
    tray = sg.SystemTray(menu=menu_def, filename=r'icon.png')
    while True:  # The event loop
        menu_item = tray.read()
        print(menu_item)
        if menu_item == 'Exit':
            break
        elif menu_item == 'Open':
            sg.popup('Menu item chosen', menu_item)


if __name__ == '__main__':
    show_tray_icon()
