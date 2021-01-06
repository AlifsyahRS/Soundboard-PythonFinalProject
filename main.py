from Soundboard import Soundboard
import tkinter as tk


def menubar(master):
    menu = tk.Menu(master)
    master.config(menu=menu)  # Creates a custom menu bar
    preferences_menu = tk.Menu(menu)
    help_menu = tk.Menu(menu)
    # Code for preferences menubar
    menu.add_cascade(label='Preferences', menu=preferences_menu)
    preferences_menu.add_command(label="Adjust")
    preferences_menu.add_command(label="Close Program", command=master.quit)
    # Code for help menubar
    menu.add_cascade(label='Help', menu=help_menu)
    help_menu.add_command(label='How to Use the Program')


def main():
    master = tk.Tk()  # Creates the GUI for the program
    master.title("Soundboard")
    menubar(master)
    Button_1 = Soundboard(1, master)
    Button_2 = Soundboard(2, master)
    Button_3 = Soundboard(3, master)
    Button_4 = Soundboard(4, master)
    Button_5 = Soundboard(5, master)
    Button_6 = Soundboard(6, master)
    Button_1.packButtons()
    Button_2.packButtons()
    Button_3.packButtons()
    Button_4.packButtons()
    Button_5.packButtons()
    Button_6.packButtons()
    master.mainloop()


if __name__ == "__main__":
    main()
