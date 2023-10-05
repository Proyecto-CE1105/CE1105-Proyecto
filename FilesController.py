import tkinter as tk
from tkinter import filedialog
import sys

class FileControllers:
    def __init__(self, music, photo):
        self.song = music
        self.music = photo
    def selectFile(self):
        root = tk.Tk()
        root.withdraw()  #Hide the tkinter window

        file_path = filedialog.askopenfilename()

        if file_path:
            print("Archivo seleccionado:", file_path)