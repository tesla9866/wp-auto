from tkinter import *
from main import mainfunx

master = Tk()
master.title("Whatsapp BOT")
w = Canvas(master, width=600, height=400)
w.config(bg='pink')
l = Label(master,text="Whatsapp Bot",height="5",fg="Blue",font=("arial",20))
l.pack()
nameinpt = Text(master,height= 2, width= 20)
nameinpt.pack()
def deliver(name):
    val = name.get('1.0',"end-1c")
    mainfunx(val)
sbmt = Button(master, text="Submit", command = lambda: deliver(nameinpt))
sbmt.pack()
mainloop()

