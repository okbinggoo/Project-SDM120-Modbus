from tkinter import *
import configparser
import os
from tkinter.ttk import Combobox
from tkinter import messagebox



poot = Tk()
poot.title("Add connection")
    
poot.geometry('450x200')
poot.resizable(width=False, height=False)

    
    
label_port= Label(poot, text="Port", width=20, font=("arial",10,"bold"))
label_port.place(x=50, y=50)

list_come = ["COM1", "COM2", "COM3", "COM4","COM5", "COM6", "COM7","COM8", "COM9", "COM10", "COM11", "COM12"]
combo = Combobox(poot, values = list_come )
combo.place(x=200, y=50)

  
    
    
##    label_baudrate = Label(poot, text="baudrate", width=20, font=("arial",10,"bold"))
##    label_baudrate.place(x=50, y=100)
##    br = Entry(poot, width=21) #9600
##    br.place(x=250, y=100)
##
##    label_Data = Label(poot, text="Data Bits", width=20, font=("arial",10,"bold"))
##    label_Data.place(x=50, y=150)
##    br = Entry(poot, width=21) #9600
##    br.place(x=250, y=150)
##
##    label_baudrate = Label(poot, text="Stop Bits", width=20, font=("arial",10,"bold"))
##    label_baudrate.place(x=50, y=200)
##    br = Entry(poot, width=21) #9600
##    br.place(x=250, y=200)
##
##    label_baudrate = Label(poot, text="Parity", width=20, font=("arial",10,"bold"))
##    label_baudrate.place(x=50, y=250)
##    br = Entry(poot, width=21) #9600
##    br.place(x=250, y=250)
##
##    label_baudrate = Label(poot, text="Tineout", width=20, font=("arial",10,"bold"))
##    label_baudrate.place(x=50, y=250)
##    br = Entry(poot, width=21) #9600
##    br.place(x=250, y=250)
    
##       

def check_write():
    com = str(combo.get())
    s = list_come
    
    if com in s:
        config = configparser.ConfigParser()
        config["portt"] = {"numberport": com }
        with open('connection.ini','w') as configfile:
            config.write(configfile)

        if(os.path.isfile('connection.ini')==True):
            answer = messagebox.showinfo("Message","Successful!!!")
            poot.destroy()
    else:
        messagebox.showinfo("Message", "Please Enter The Message Again")

   
        
def disable_event():
    pass      
    

b4= Button(poot, text="Submit", width=12,bg='brown',fg='white',command=check_write)
    
b4.place(x=220,y=100)

poot.protocol("WM_DELETE_WINDOW", disable_event)
    
poot.mainloop()


        
