from tkinter import *
 
window = Tk()
window.title("NewsCast for Prady")

newslist = Label(window, text="Select Category", font=("Arial Bold", 20))
newslist.grid(column=0, row=0)

#button
# btn = Button(window, text='Button')
# btn.grid(column=1, row=0)
# def clicked():
#     newslist.configure(text="Button was clicked")
# btn = Button(window, text='Button', command=clicked)



window.geometry('1024x768')

window.mainloop()