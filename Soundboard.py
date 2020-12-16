
# Used for creating a file explorer to select a file.
import tkinter as tk
from playsound import playsound
from tkinter import filedialog


class Soundboard():
    def __init__(self, button_num):
        self.button_num = int(button_num)
        self.file = None

    def setFile(self):
        self.file = filedialog.askopenfilename(
            filetypes=[("Mp3 Files", "*.mp3")]).replace(" ", "%20")
        # When executed, this function will create a file explorer wherein the user can choose top open the audio files the choose.
        # Replace is needed because the playsound module cannot reach a directory which contains a space character in its name

    def getFileDir(self):
        return self.file

    def playSound(self):
        if self.file == None:
            return(f"Button {self.button_num} cannot be used because no file has been assigned.")
        else:
            playsound(self.file)
            return("Playing sound")

    def Button(self, m):
        play_button = tk.Button(master=m, text=f'Audio {self.button_num}', width=10,
                                height=5, command=self.playSound)
        select_file = tk.Button(master=m, text=f'Change File {self.button_num}',
                                width=10, height=5, command=self.setFile)
        play_button.pack()
        select_file.pack()
