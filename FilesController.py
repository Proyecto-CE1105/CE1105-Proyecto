import tkinter as tk, os
from tkinter import filedialog
import sys

class FileControllers:
    def __init__(self, music, photo):
        self.song = music
        self.photo = photo
    def selectFile(self):
        root = tk.Tk()
        root.withdraw()  #Hide the tkinter window

        file_path = filedialog.askopenfilename()
        self.photo = os.path.basename(file_path)
        self.song = os.path.basename(file_path)
        if file_path:
            print("Archivo seleccionado:", str(file_path))