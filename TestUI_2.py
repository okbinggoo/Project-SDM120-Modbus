from tkinter import *
import configparser
import os
from tkinter.ttk import Combobox
from tkinter import messagebox

import time

def call_port():
    os.system('Edit_port.py')

root = Tk()
root.title("SDM20 Program") 

root.geometry('840x400')
root.resizable(width=False, height=False)

label0= Label(root, text="ID Slave", width=20, font=("arial",10,"bold"))
label0.place(x=140,y=110)

label1= Label(root, text="SDM20", relief="solid", width=20, font=("arial",19,"bold"))
label1.place(x=165,y=53)

label2= Label(root,text="Register Address",width=20,font=("arial",10,"bold"))
label2.place(x=140,y=150)

label2= Label(root,text="ID slave & Register address",width=30,font=("arial",10,"bold"))
label2.place(x=470,y=53)

##label2= Label(root,text="Data type",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=190)
##
##label2= Label(root,text="Read type",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=230)

##label2= Label(root,text="Refresh time",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=270)

#register address
e = Entry(root, width=21) #Register
e.place(x=340, y=150)

e1 = Entry(root, width=21) #Slave
e1.place(x=340, y=110)

###data type
##e1 = Combobox(root, width=18)
##e1['values'] = ("Coil status (0xxxx)","Input status (1xxxx)","Input register (3xxxx)", "Holding register (4xxxx)")
##e1.current(0)
##e1.place(x=340, y=190)
##
###read type
##e2 = Combobox(root, width=18)
##e2['values'] = ("Float", "Uint",)
##e2.current(0)
##e2.place(x=340, y=230)

#time refresh
##e3 = Entry(root, width=21)
##e3.place(x=340, y=190)

    
def checkError():
    a=0
    string = e.get()
    string1 = e1.get()
    
    if(string.isnumeric()==False):
        messagebox.showinfo("Message", "The register should be number!!")
        a+=1
    if(string1.isnumeric()==False):
        messagebox.showinfo("Message", "The Slave ID should be number!!")
        a+=1

    else:
        b = int(e.get())
        b1 = int(e1.get())
        if(b>225 or b<0):
            messagebox.showinfo("Message", "Register number should be 0-225!!")
            a+=1
        if(b1<0):
            messagebox.showinfo("Message","Slave ID must > 0")
            a+=1
    return a


def Adding():
    a=checkError()
    if(a<1):
        config = configparser.ConfigParser()
        temp = e.get()
##        temp1 = e1.get()
##        if(e1.get()== "Input status (1xxxx)"):
##            temp1 = 1
##        elif(e1.get()=="Holding register (4xxxx)"):
##            temp1 = 4
##        elif(e1.get()=="Coil status (0xxxx)"):
##            temp1 = 0
##        else:
##            temp1 = 3
##            
##        temp2 = e2.get()
##        if(e2.get()=="Float"):
##            temp2 = 1
##       else:
##            temp2 = 2
##
        item = str(e1.get())
        ID = "ID"+item
        t=0
##        temp3 = e3.get()
        a1 = [ID,temp,t]
        print(a1)

        coulis = listbox1.size()
        listbox1.insert(coulis, "Data added!")
        listbox1.insert(coulis+1, a1[0]) #add id to list1
        print("add id: ",coulis)
        listbox1.insert(coulis+2, a1[1]) #add register
        listbox1.insert(coulis+3, "")
        
        if(os.path.isfile('config.ini')==False):
            
            config[a1[0]] = {"Register": a1[1]}
            with open('config.ini','w') as configfile:
                config.write(configfile)
        else:
            config.read('config.ini')
            config[a1[0]] = {"Register": a1[1]}
            with open('config.ini','w') as configfile:
                config.write(configfile)
            
        messagebox.showinfo("Message", "Add register successful!!")

        return a1
    else:
        messagebox.showinfo("Message", "Please try again")

    
    
        

def show_data():
    import show_data_2
    show_data_2.main()
    path = 'Get_data.ini'
    
    section = get_section(path)
    #print(section)
    #a = get_setting(path, section[0],"Answer")
    #messagebox.showinfo(title='Register data', message="Report Result!" '\n' 'Id slave: %s' '\n' 'The result from register %s \n = %s' %(b[0],b[1], a))
    conta = len(section)
    listans= []
    i=0
    while i < conta:
        a = get_setting(path, section[i],"Answer")
##        messagebox.showinfo(title='Register data', message="Report Result!" '\n' 'Id slave: %s' '\n' ' = %s' %(section[i], a))
        listans.append(a)
        print(listans)
        if(i+1==conta):
            print(listans)
            #ReadAllIndex()
            show_message(listans)
        i+=1

def show_data_1():
    import show_data_2
    show_data_2.main()
    path = 'Get_data.ini'
    
    section = get_section(path)
    #print(section)
    #a = get_setting(path, section[0],"Answer")
    #messagebox.showinfo(title='Register data', message="Report Result!" '\n' 'Id slave: %s' '\n' 'The result from register %s \n = %s' %(b[0],b[1], a))
    conta = len(section)
    listans= []
    i=0
    while i < conta:
        a = get_setting(path, section[i],"Answer")
##        messagebox.showinfo(title='Register data', message="Report Result!" '\n' 'Id slave: %s' '\n' ' = %s' %(section[i], a))
        listans.append(a)
        print(listans)
        i+=1
    return listans

def show_message(listans):
    import show_data_2
    path = 'config.ini'
    section = get_section(path)
    boot = Tk()
    boot.title("Show list of register")
    
    boot.geometry('300x250')
    boot.resizable(width=False, height=False)
    


    bo= Button(boot, text="Stop", width=12,bg='brown',fg='white',command=boot.destroy)
    bo.pack()

    listbox0 = Listbox(boot)
    listbox0.pack()
    

    count = len(listans)
    
    while True:
        a = listbox0.size()
        while(a>=0):
            listbox0.delete(a)
            a-=1
        for i in range(count):
            re = get_setting(path, section[i],"register")
            listbox0.insert(END, "Register"+" "+re+": "+listans[i])

        show_data_2.main()
        listans = show_data_1()
        time.sleep(2)  
        boot.update()
    boot.mainloop()


def ReadAllIndex():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    for sect in parser.sections():
       print(sect)
       for k,v in parser.items(sect):
          print(' {} = {}'.format(k,v))
       print()  

def new_P():
    a = listbox1.size()
    i = 0
    if(os.path.isfile('config.ini')==True): #delete all data
        os.remove("config.ini")
        if(os.path.isfile('Get_data.ini')==True):
            os.remove("Get_data.ini")
        while(a>=0):
            listbox1.delete(a)
            a-=1
        messagebox.showinfo(title='Message', message="All data removed")
    else:
        messagebox.showinfo(title='Message', message='No adding')        
def exit1():
    answer = messagebox.askyesno("exit","Do you really want to exit")
    if(os.path.isfile('config.ini')==True): # Delete all data before exit
        os.remove("config.ini")
        if(os.path.isfile('Get_data.ini')==True):
            os.remove("Get_data.ini")
    if(answer):
        root.destroy()
        

def get_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, sett):
    config = get_config(path)
    value = config.get(section, sett)
    msg = "{section} {sett} = {value}".format(
        section=section, sett=sett, value=value)
    return value

def get_section(path):
    config = get_config(path)
    sect = config.sections()
    return sect

def disable_event():
    pass   #remove X


##myButton = Button(root, text="Click Me", command=myClick)
b1= Button(root, text="Add", width=12,bg='brown',fg='white',command=Adding)
b1.place(x=220,y=195)

b11= Button(root, text="Exit", width=12,bg='brown',fg='white',command=exit1)
b11.place(x=320,y=250)

b2=Button(root, text="Scan",width=12,bg='brown',fg='white',command=show_data)
b2.place(x=320,y=195)

##b4= Button(root, text="Show", width=12,bg='brown',fg='white',command=Insert_L)
##b4.place(x=220,y=250)

b3= Button(root, text="Reset", width=12,bg='brown',fg='white',command=new_P)
b3.place(x=220,y=250)

b3= Button(root, text="Edit Port", width=12,bg='brown',fg='white',command=call_port)
b3.place(x=70,y=250)



listbox1 = Listbox(root, width=50, heigh=15)
listbox1.place(x=500,y=80)

root.protocol("WM_DELETE_WINDOW", disable_event)

root.mainloop()
