import RPi.GPIO as rp
rp.setmode(rp.BOARD)
rp.setwarnings(False)
p=[29,31,33,35,37]
for i in p:
    rp.setup(i,rp.OUT)
rp.setup(11,rp.IN)
while(1):
    if(rp.input(11)==1):
        rp.output(29,0)
        rp.output(31,0)
        rp.output(33,0)
        rp.output(35,0)
        rp.output(37,0)
        print("All Lights are Off")
    else:
        rp.output(29,1)
        rp.output(31,1)
        rp.output(33,1)
        rp.output(35,1)
        rp.output(37,1)
        print("All Lights are On")


