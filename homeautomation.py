import RPi.GPIO as rp
import time as t
import requests
import Adafruit_DHT
rp.setwarnings(False)
rp.setmode(rp.BCM)
rp.setup(4,rp.OUT)
rp.setup(17,rp.OUT)
rp.setup(27,rp.OUT)
rp.setup(22,rp.OUT)
rp.setup(18,rp.OUT)
rp.setup(23,rp.OUT)
rp.setup(13,rp.OUT)
rp.setup(19,rp.IN)
rp.setup(26,rp.OUT)
rp.setup(21,rp.IN)
count=0
def caldis1():
    rp.output(13,1)
    t.sleep(0.0001)
    rp.output(13,0)
    while(rp.input(19)==0):
        pass
    st=t.time()
    while(rp.input(19)==1):
        pass
    stopt=t.time()
    tt=stopt-st
    d=34300*tt/2
    return d

def caldis2():
    rp.output(26,1)
    t.sleep(0.0001)
    rp.output(26,0)
    while(rp.input(21)==0):
            pass
    st=t.time()
    while(rp.input(21)==1):
            pass
    stopt=t.time()
    tt=stopt-st
    d=34300*tt/2
    return d
c=int(input("Choose your mode\n1.For manuual\n2.For automation\n"))
if(c==1):
    print("Mannual mode selected")
while(1):
    r=requests.get("http://indianiotcloud.com/retrieve.php?id=N7BXFL2NUZ5YIMRY3KSM")
    d=r.json()
    b1=int(d['result'][0]['field1'])
    if(b1==1):
        rp.output(4,0)
        print(' bulb1 started')
    else:
        rp.output(4,1)
        print("bulb1 Stopped")
    b2=int(d['result'][0]['field2'])
    if(b2==1):
        rp.output(17,0)
        print(' bulb2 started')
    else:
        rp.output(17,1)
        print("bulb2 Stopped")          
    f1=int(d['result'][0]['field3'])
    if(f1==1):
        rp.output(18,1)
        print("Fan 1 started")

       
    else:
        rp.output(18,0)
        print("Fan 1 stopped")
                      
    f2=int(d['result'][0]['field4'])
    if(f2==1):
        rp.output(23,1)
        print("Fan 2 started")
        
    else:
        rp.output(23,0)
        print("Fan 2 stopped")
      
if(c==2):
    print("automatic mode selected")
while(1):
    dis=caldis1()
    if(dis<20):
        count=count+1
        print(count)
      
    dis1=caldis2()
    if(dis1<20):
        count=count-1
        print(count)
    humidity,temperature=Adafruit_DHT.read_retry(11,25)
    if(count>0):
        if(rp.input(22)==1):
            rp.output(4,1)
            print("bulb1 Started")
        else:
            rp.output(4,0)
            print("bulb1 Stopped")
        if(rp.input(27)==1):
            rp.output(17,1)
            print("bulb2 started")
        else:
            rp.output(17,0)
            print("bulb2 stopped")
            
        if(temperature>=30):
            print(temperature)
            rp.output(18,1)
            print("Fan 1 started")
            rp.output(23,1)
            print("Fan 2 started")
        else:
            rp.output(18,0)
            print("Fan 1 stopped")
            rp.output(23,0)
            print("Fan 2 stopped")
