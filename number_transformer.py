import tkinter
from tkinter import filedialog, font, messagebox

class NumberTransformerGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Number Transformer Pro")
        self.main_window.geometry("500x450")
        self.main_window.configure(bg="#2d3436")