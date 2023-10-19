from tkinter import *

ws = Tk()
ws.title('PythonGuides')


img = PhotoImage(file=r'C:\Users\prosi\OneDrive\Dokumenty\GitHub\Main\PolAng\photos\airport.png')
Label(
    ws,
    image=img,
    height=2,
    width=2
).pack()

ws.mainloop()