import tkinter as tk
from tkinter import filedialog
import os


class FileControllers:
    def __init__(self, music, photo):
        self.music = music
        self.photo = photo
    def selectFile(self, data):
        root = tk.Tk()
        root.withdraw()  #Hide the tkinter window

        file_path = filedialog.askopenfilename()
        if data == "music":
            self.music = os.path.basename(file_path)
            print(self.music)
        elif data == "photo":
            self.photo = os.path.basename(file_path)
            print(self.photo)