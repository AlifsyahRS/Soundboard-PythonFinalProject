
# Used for creating a file explorer to select a file.
import tkinter as tk
from playsound import playsound
from tkinter import filedialog


class Soundboard():
    def __init__(self, button_num):
        self.button_num = int(button_num)
        self.file = None
        self.button_label = f"Audio {self.button_num}"

    def setFile(self):
        self.file = filedialog.askopenfilename(
            filetypes=[("Mp3 Files", "*.mp3")]).replace(" ", "%20")
        # When executed, this function will create a file explorer wherein the user can choose top open the audio files the choose.
        # Replace is needed because the playsound module cannot reach a directory which contains a space character in its name

    def getFileDir(self):
        return self.file

    def setButtonLabel(self, new_label):
        self.button_label = new_label

    def playSound(self):
        if self.file == None:
            pass
        else:
            playsound(self.file)

    def packButton(self, master):
        frame = tk.Frame(master)
        frame.pack()
        play_button = tk.Button(frame, text=self.button_label, width=10,
                                height=5, command=self.playSound)
        play_button.pack(side=tk.LEFT)
        changefile_button = tk.Button(
            frame, text="^", width=3, height=3, command=self.setFile)
        changefile_button.pack(side=tk.RIGHT)
        play_button.pack()
