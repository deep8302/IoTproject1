from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time as t
root = Tk()
root.title("Smart City login")
root.geometry("1600x800")
root.configure(background="light blue")

username=StringVar()
password=StringVar()

def uname():
    d=username.get()
    auname="smartcity"
    if(auname==d):
        pswd=Label(font=('arial',20),text="Password",bg="light blue",bd=5,relief=RIDGE).place(x=550,y=400)
        pswd1=Entry(f1,width=15,bd=5,font=('arial',18),textvariable=password,show="*").place(x=700,y=400)
        def pswd():
            apass="iot"
            p=password.get()
            if(apass==p):
                root.destroy()
                import os
                os.system('python test.py')
                t.sleep(2)
                
            else:
                messagebox.showinfo(title='warning',message='Invalid password Please try again')
                password.set("")
        bt1=Button(text="Submit",padx=15,pady=8,font=('arial',15,'bold'),relief=GROOVE,command=pswd).place(x=600,y=500)
    else:
        messagebox.showinfo(title='warning',message='Invalid User Name Please try again')
        username.set("")
#------------------------------first frame---------------------------------------------------------------------------------
        
Tops=Frame(root, width=1600,height=100, relief=SUNKEN,bg="light blue").pack(side=TOP)

f1=Frame(root, width=500,height=500,relief=SUNKEN,bg="light blue").place(x=500,y=150)

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Smart city 2.0",fg="red",bg="light blue",anchor='w').place(x=500,y=50)
#------------------------------------------------------------------------------------------------------------------
label1=Label(font=('arial',30,'bold'),text="Login",fg="red",bg="light blue",relief=RAISED).place(x=650,y=200)

u=Label(font=('arial',20),text="Username",bd=5,relief=RIDGE,bg="light blue").place(x=550,y=350)
ut=Entry(f1,width=15,bd=5,font=('arial',18),textvariable=username).place(x=700,y=350)

bt1=Button(text="Submit",padx=15,pady=8,font=('arial',15,'bold'),relief=GROOVE,command=uname).place(x=600,y=500)
bt2=Button(text="Exit",padx=15,pady=8,font=('arial',15,'bold'),relief=GROOVE,width=6,command=root.destroy).place(x=720,y=500)

#------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()
