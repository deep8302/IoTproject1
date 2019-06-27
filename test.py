from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Smart city")
root.geometry("2289x1754")
root.configure(background="light blue")
def hospital():
    import os
    os.system("python hospital.py")

def light():
    import os
    os.system("python street.py")

def dustbin():
    import os
    os.system("python sm_dust.py")

def parking():
    import os
    os.system("python smartpark.py")

def farmer():
    import os
    os.system("python crops.py")
    os.system("python dht11_py.py")

def toll():
    import os
    os.system("python Toll_tax.py")
    
def home():
    import os
    os.system("python homeautomation.py")


##image = Image.open('city3.png')
##photo_image = ImageTk.PhotoImage(image)
##label = Label(root, image = photo_image).pack()

lbl=Label(root,font=("arial",40,"bold"),text="Welcome to city control pannel",fg="red",bg="light blue",justify="center").pack()

btn1=Button(root,text="hospital",padx=10,pady=10,font=("arial",20,"bold"),command=hospital).place(x=310,y=100)     

btn2=Button(root,text="StreetLight",padx=10,pady=10,font=("arial",20,"bold"),command=light).place(x=310,y=200)

btn3=Button(root,text="Smart Dustbin",padx=10,pady=10,font=("arial",20,"bold"),command=dustbin).place(x=310,y=300)

btn4=Button(root,text="Smart parking",padx=10,pady=10,font=("arial",20,"bold"),command=parking).place(x=600,y=100)

btn5=Button(root,text="Smart irrigation",padx=10,pady=10,font=("arial",20,"bold"),command=farmer).place(x=600,y=200)

btn6=Button(root,text="Toll Tax",padx=10,pady=10,font=("arial",20,"bold"),command=toll).place(x=600,y=300)

btn7=Button(root,text="Home Automation",padx=10,pady=10,font=("arial",20,"bold"),command=home).place(x=400,y=400)
root.mainloop()
