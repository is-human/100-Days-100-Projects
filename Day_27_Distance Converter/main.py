from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=300, height=100)

def button_clicked():
    calculated_km["text"] = float(miles.get()) * 1.60934

text_1 = Label(text="is equal to")
text_1.grid(row=2, column=1)

miles = Entry(width=7)
miles.grid(row=1, column=2)

calculated_km = Label(text=0)
calculated_km.grid(row=2, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

text_mi = Label(text="Miles")
text_mi.grid(row=1, column=3)

text_km = Label(text="Km")
text_km.grid(row=2, column=3)

window.mainloop()