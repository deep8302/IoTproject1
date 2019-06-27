from tkinter import *
from tkinter import messagebox
import urllib.request
import webbrowser as wb
def kc():
    c=wb.open("https://en.wikipedia.org/wiki/Kharif_crop")
def rb():
    p=wb.open("https://en.wikipedia.org/wiki/Rabi_crop")
def zc():
    l=wbopen("https://en.wikipedia.org/wiki/Zaid_crops")
root=Tk()
root.title("Farmer guide")
root.geometry('600x500')
root.configure(background="light blue")
l=Label(text="Welcome to farmer guide",font=("arial",20,"bold"),fg="red",bg="light blue").pack()
l2=Label(text="please choose your crope",font=("arial",15,"bold"),fg="black",bg="light blue",justify="right").pack()
f=Button(root,font=('arial',15,'bold'),text="kharif crop",width=40,command=kc,justify="center")
f.place(x=50,y=120)
f=Button(root,font=('arial',15,'bold'),text="rabi crops",width=40,command=kc,justify="center")
f.place(x=50,y=220)
f=Button(root,font=('arial',15,'bold'),text="Zaid crop",width=40,command=kc,justify="center")
f.place(x=50,y=320)
root.mainloop()


