import tkinter as tk
from tkinter import filedialog
import os


class FileControllers:
    def __init__(self, music, photo):
        self.music = music
        self.photo = photo
    def selectFile(self):
        root = tk.Tk()
        root.withdraw()  #Hide the tkinter window

        file_path = filedialog.askopenfilename()
        self.photo = os.path.basename(file_path)
        self.music = os.path.basename(file_path)
        if file_path:
            print("Archivo seleccionado:", str(file_path))
