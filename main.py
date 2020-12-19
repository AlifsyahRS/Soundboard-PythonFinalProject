from Soundboard import Soundboard
import tkinter as tk

Button_1 = Soundboard(1)
Button_2 = Soundboard(2)
Button_3 = Soundboard(3)
Button_4 = Soundboard(4)
Button_5 = Soundboard(5)
Button_6 = Soundboard(6)


def menubar(master):
    menu = tk.Menu(master)
    master.config(menu=menu)
    settingsmenu = tk.Menu(menu)
    helpmenu = tk.Menu(menu)
    menu.add_cascade(label='Settings', menu=settingsmenu)
    # For settings menubar
    settingsmenu.add_command(label="Change Volume (WIP)")
    settingsmenu.add_command(label="Close Program", command=master.quit)
    # For help menubar
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='How to Use the Program')


def main():
    master = tk.Tk()
    menubar(master)
    Button_1.packButton(master)
    Button_2.packButton(master)
    Button_3.packButton(master)
    Button_4.packButton(master)
    Button_5.packButton(master)
    Button_6.packButton(master)
    master.mainloop()


if __name__ == "__main__":
    main()
