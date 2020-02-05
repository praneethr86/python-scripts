from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("NewsCast for Prady")

#Todo: use Frame/Paned Window/LabelFrame to arrange widgets, Text for showing content, scrollbar ( in both listbox and text pane), Message box for alerting.

#button
# btn = Button(window, text='Button')
# btn.grid(column=1, row=0)
# def clicked():
#     newslist.configure(text="Button was clicked")
# btn = Button(window, text='Button', command=clicked)

window.geometry('1024x768')

# txt = scrolledtext.ScrolledText(window, width=50, height=100)
# txt.grid(column=0, row=1)

newslist = Label(window, text="Select Category", font=("Arial Bold", 20))

listbox = Listbox(window)

listbox.insert(1, "The Hindu")
listbox.insert(2, "HBR")
listbox.insert(3, "The Economist")
listbox.insert(4, "TechCrunch")
listbox.insert(5, "ESPN F1")
listbox.insert(6, "EPL")

newslist.pack()
listbox.pack()



window.mainloop()