import time as t
import RPi.GPIO as rp
import smtplib as s
rp.setmode(rp.BOARD)
rp.setwarnings(False)
l=[11,13,21,31,33,35,37]

def distance():
    rp.output(21,1)
    t.sleep(0.001)
    rp.output(21,0)
    while(rp.input(19)==0):
            pass
    st=t.time()
    while(rp.input(19)==1):
            pass
    stopt=t.time()
    tt=stopt-st
    d=34300*tt/2
    return d

rp.setup(19,rp.IN)
for i in l:
    rp.setup(i,rp.OUT)
    
def checked(c):
    if((c&0x01)==0):
        rp.output(11,0)
    else:
        rp.output(11,1)

    if((c&0x02)==0):
        rp.output(13,0)
    else:
        rp.output(13,1)

    if((c&0x10)==0):
        rp.output(31,0)
    else:
        rp.output(31,1)

    if((c&0x20)==0):
        rp.output(33,0)
    else:
        rp.output(33,1)

    if((c&0x40)==0):
        rp.output(35,0)
    else:
        rp.output(35,1)

    if((c&0x80)==0):
        rp.output(37,0)
    else:
        rp.output(37,1)

def cmd(c):
    d=c&0xF0
    d=d+0x02
    checked(d)
    t.sleep(0.001)
    d=d-0x02
    checked(d)
    d=(c<<4)&0xf0
    d=d+0x02
    checked(d)
    t.sleep(0.001)
    d=d-0x02
    checked(d)

def data(c):
    d=c&0xF0
    d=d+0x03
    checked(d)
    t.sleep(0.001)
    d=d-0x02
    checked(d)
    d=(c<<4)&0xf0
    d=d+0x03
    checked(d)
    t.sleep(0.001)
    d=d-0x02
    checked(d)
    
def init():
    cmd(0x02)
    cmd(0x28)
    cmd(0x06)
    cmd(0x0C)

def clear():
    cmd(0x01)
    t.sleep(0.001)

    
init()
def string(s):
    l=len(s)
    for i in range(0,l):
        data(ord(s[i]))
cmd(0x80)  

        
while(1):
    clear()
    dis=distance()
    if(dis<20):
        print("keep going")
        string('Dustbin is full')
        cmd(0xc0)
        string("mail sent")
        t.sleep(2)
    else:
        print("empty now")
        string("*Smart Dustbin*")
        cmd(0xc0)
        string("**it's empty now**")
        t.sleep(2)
