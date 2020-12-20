import tkinter as tk
from playsound import playsound
# Used for creating a file explorer to select a file.
from tkinter import filedialog


class Soundboard():
    def __init__(self, button_num, master):
        self.button_num = int(button_num)
        self.file = None
        self.button_label = f"Audio {self.button_num}"
        self.master = master

    def setFile(self):
        self.file = filedialog.askopenfilename(
            filetypes=[("Mp3 Files", "*.mp3"), ("Uncompressed Audio Files", "*.wav")]).replace(" ", "%20")
        # When executed, this function will create a file explorer wherein the user can choose top open the audio files the choose.
        # Replace is needed because the playsound module cannot reach a directory which contains a space character in its name

    def playSound(self):
        if self.file == None:
            # Nothing happens if no file is chosen.
            pass
        else:
            # playsound() plays the audio file
            playsound(self.file)

    def setButtonLabel(self):
        rename_window = tk.Toplevel(self.master)
        rename_str = tk.StringVar()  # Storage for user input
        rename_entry = tk.Entry(rename_window, bd=5)
        rename_entry.pack(side=tk.LEFT)
        rename_button = tk.Button(
            rename_window, text="Enter", bd=5, command=rename_entry.get)
        rename_button.pack(side=tk.RIGHT)
        rename_str.set(rename_button)
        self.button_label = rename_str.get()

    def buttonPreferences(self):
        new_window = tk.Toplevel(self.master)
        setfile_button = tk.Button(
            new_window, text="Swap Current\nAudio File", width=10, height=5, command=self.setFile)
        setfile_button.pack()
        change_buttonlabel = tk.Button(
            new_window, text="Rename Button\n(WIP)", width=10, height=5, command=self.setButtonLabel)
        change_buttonlabel.pack()

    def packButton(self):
        # I used a frame object to help organize the buttons
        frame = tk.Frame(self.master)
        frame.pack()  # .pack() puts objects into the master window of the program
        # Button object creates buttons
        play_button = tk.Button(frame, text=self.button_label, width=10,
                                height=5, command=self.playSound)
        # side parameter puts the button in a specific position relative to the frame
        play_button.pack(side=tk.LEFT)
        button_preferences = tk.Button(
            frame, text="^", width=3, height=3, command=self.buttonPreferences)
        button_preferences.pack(side=tk.RIGHT)
