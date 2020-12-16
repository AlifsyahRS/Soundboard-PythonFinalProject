from Soundboard import Soundboard
import tkinter as tk

Button_1 = Soundboard(1)
Button_2 = Soundboard(2)


def main():
    m = tk.Tk()
    Button_1.Button(m)
    Button_2.Button(m)
    m.mainloop()


if __name__ == "__main__":
    main()
