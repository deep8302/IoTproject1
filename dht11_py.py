import RPi.GPIO as io
import sys
import Adafruit_DHT
import time
io.setmode(io.BCM)
io.setwarnings(False)
io.setup(7,io.out)
h=40

while (1):
    Humidity,Temperature=Adafruit_DHT.read_retry(11,4)
    print("Temperature: {0:0.1f} C Humidity: {1:0.1f} %".format (Temperature,Humidity))
    time.sleep(1)
    if humidity > h:
        io.output(7,1)
    else:
        io.output(7,0)
        
    
