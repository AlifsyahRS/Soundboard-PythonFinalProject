from Soundboard import Soundboard
import tkinter as tk


def main():
    master = tk.Tk()  # Creates the GUI for the program
    master.title("Soundboard")
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
