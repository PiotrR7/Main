import tkinter as tk
from easy_mode import *
from medium_mode import *
from hard_mode import *

class Memory:
    window = tk.Tk()
    chosen_level = ""

class Apk:
    def Window():
        Memory.window.resizable(False,False)
        Memory.window.title("")
        Memory.window.geometry("700x300")

        btn_ey = tk.Button(text="Easy", width=20, height=3, command=lambda: Apk.Level("easy")).place(x=70, y=100)
        btn_mm = tk.Button(text="Medium", width=20, height=3, command=lambda: Apk.Level("medium")).place(x=270, y=100)
        btn_hd = tk.Button(text="Hard", width=20, height=3, command=lambda: Apk.Level("hard")).place(x=470, y=100)

        Memory.window.mainloop()
    
    def Level(arg):
        Memory.chosen_level = arg
        Memory.window.destroy()
        if (Memory.chosen_level == "easy"):
            EasyMode.Play()
        if (Memory.chosen_level == "medium"):
            MediumMode.Play()
        if (Memory.chosen_level == "hard"):
            HardMode.Play()

Apk.Window()