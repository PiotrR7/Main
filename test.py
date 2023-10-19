import tkinter as tk

root = tk.Tk()
yellow = tk.PhotoImage(file=r'PolAng\photos\apple.png')

string = "yellow"


photos = [yellow]
photosstr = ["yellow"]



label = tk.Label(image=photos[photosstr.index(string)]).pack()

root.mainloop()