from tkinter import *
 
window = Tk()
window.title("NewsCast for Prady")

newslist = Label(window, text="Select Category", font=("Arial Bold", 20))
newslist.grid(column=0, row=0)

window.geometry('1024x768')

window.mainloop()