import xlrd as xr
import xlwt as xw
import serial
import vlc
import time as t
import RPi.GPIO as rp
rp.setwarnings(False)
rp.setmode(rp.BOARD)
rp.setup(7,rp.OUT)
rp.setup(11,rp.IN)
rp.setup(13,rp.OUT)
rp.setup(15,rp.OUT)
rp.setup(19,rp.OUT)
rp.setup(23,rp.OUT)
rp.setup(21,rp.IN)
name=[]
nc=5
s=serial.Serial('/dev/ttyUSB0')
d=s.read(12)
print (d)
n=0
print('CARD ACCEPTED')
na=input('NAME:')
name.append(na)
instance=vlc.Instance()
player=instance.media_player_new()
ch='welcome.mp3'
media=instance.media_new(ch)
media.get_mrl()
player.set_media(media)
player.play()

t.sleep(5)
wb=xw.Workbook()
shw=wb.add_sheet('sheet1')
for i in range(0,len(name)):
    shw.write(0,i,name[i])
wb.save('Parking.xls')
instance=vlc.Instance()
player=instance.media_player_new()
ch='welcome1.mp3'
media=instance.media_new(ch)
media.get_mrl()
player.set_media(media)
player.play()

t.sleep(2)
rp.output(7,1)
rp.output(15,0)
t.sleep(10)
rp.output(7,0)
rp.output(15,1)
t.sleep(5)
rp.output(15,0)

rp.output(19,1)
t.sleep(0.0001)
rp.output(19,0)
while(n<5):
    while(rp.input(11)==0):
        pass
    st=t.time()
    while(rp.input(11)==1):
        pass
    sot=t.time()
    tt=sot-st
    d=(34300*tt)/2
    if(d<100):
        print('car is at distance',d,'cm')
    n=n+1
    if( d<=5):
        print('The Car is parked rightly')
        rp.output(13,1)
        t.sleep(10)
        rp.output(13,0)
    t.sleep(2)
rp.output(23,1)
t.sleep(0.0001)
rp.output(23,0)
while(n<5):
    while(rp.input(21)==0):
        pass
    st=t.time()
    while(rp.input(21)==1):
        pass
    sot=t.time()
    tt=sot-st
    d=(34300*tt)/2
    if(d<100):
        print('car is at distance',d,'cm')
    n=n+1
    if( d<=5):
        print('The Car is parked rightly')
        rp.output(13,1)
        t.sleep(10)
        rp.output(13,0)
    t.sleep(2)

    
    
