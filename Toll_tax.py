import RPi.GPIO as IO
import serial
import xlrd
import xlwt
from xlutils.copy import copy
import time
data=xlrd.open_workbook('Toll_Tax.xls')
table=data.sheet_by_index(1)
r=table.nrows
c=table.ncols
ser=serial.Serial('/dev/ttyUSB0',9600)
print("********** TOLL TAX PROGRAM ***********")
print("S.No.\t\tVehicle\t\tSingle\t\tDouble")
print("1.\t\tCar\t\t120\t\t200")
print("2.\t\tTruck\t\t200\t\t350")
print("3.\t\tBuses\t\t150\t\t250")
print("Park The Vehicle")
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(3,IO.IN)
IO.setup(7,IO.OUT)

IO.setup(31,IO.OUT)                # initialize GPIO Pins as outputs
IO.setup(15,IO.OUT)
IO.setup(40,IO.OUT)
IO.setup(38,IO.OUT)
IO.setup(36,IO.OUT)
IO.setup(32,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(18,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(12,IO.OUT)

def send_a_command (command):                # execute the loop when “sead_a_command” is called
    pin=command
    PORT(pin);                                                # calling 'PORT' to assign value to data port
    IO.output(31,0)                                           # putting 0 in RS to tell LCD we are sending command
    IO.output(15,1)                                         # telling LCD to receive command/data at the port by pulling EN pin high
    time.sleep(0.05)
    IO.output(15,0)                                         # pulling down EN pin to tell LCD we have sent the data.
    pin=0
    PORT(pin);                                                # pulling down the port to stop transmitting

def send_a_character (character):                # execute the loop when “send_a_character” is called
    pin=character
    PORT(pin);
    IO.output(31,1)
    IO.output(15,1)
    time.sleep(0.05)
    IO.output(15,0)
    pin=0
    PORT(pin);

def PORT(pin):                                # assigning PIN by taking PORT value
    if(pin&0x01 == 0x01):
        IO.output(40,1)                        # if  bit0 of 8bit 'pin' is true, pull PIN21 high
    else:
        IO.output(40,0)                        # if  bit0 of 8bit 'pin' is false, pull PIN21 low
    if(pin&0x02 == 0x02):
        IO.output(38,1)                        # if  bit1 of 8bit 'pin' is true, pull PIN20 high
    else:
        IO.output(38,0)                        # if  bit1 of 8bit 'pin' is true, pull PIN20 low
    if(pin&0x04 == 0x04):
        IO.output(36,1)
    else:
        IO.output(36,0)
    if(pin&0x08 == 0x08):
        IO.output(32,1)
    else:
        IO.output(32,0)   
    if(pin&0x10 == 0x10):
        IO.output(22,1)
    else:
        IO.output(22,0)
    if(pin&0x20 == 0x20):
        IO.output(18,1)
    else:
        IO.output(18,0)
    if(pin&0x40 == 0x40):
        IO.output(16,1)
    else:
        IO.output(16,0)
    if(pin&0x80 == 0x80):
        IO.output(12,1)                        # if  bit7 of 8bit 'pin' is true pull PIN18 high
    else:
        IO.output(12,0)                       #if  bit7 of 8bit 'pin' is false pull PIN18 low
			    
send_a_command(0x01);                    # sending 'all clear' command
send_a_command(0x38);                    # 16*2 line LCD
send_a_command(0x0E);                    # screen and cursor ON
send_a_character(0x57);                    # ASCII code for 'C'
send_a_character(0x45);                    # ASCII code for 'I' 
send_a_character(0x4c);                    # ASCII code for 'R'
send_a_character(0x43);                    # ASCII code for 'C'
send_a_character(0x4f);                    # ASCII code for 'U' 
send_a_character(0x4d);                    # ASCII code for 'I' 
send_a_character(0x45);                    # ASCII code for 'T'

while(1):
    while(1):
        if(IO.input(3)==1):
            IO.output(7,1)
            print("\n\nVehicle Detected")
            break
        else:
            continue
    print("Sir Please Show Me Your Card")
    print("swipe your card : ")
    ser.close()
    ser.open()
    card=ser.read(12)
    card=card.decode("utf-8")
    
    ser.close()
    print(card)
    for i in range(1,r):
        
        k=table.cell_value(i,1)
        if(card==k):
            ask=input("Can You Please Tell Me The route \n1. for Single\n2.Double\n")
            if(ask==1):
                ch=int(input("Choose your Vehicle type from above list (1-3) : \n"))
                if(ch==1):
                    print("Your Fare Is 120")
                    wb=copy(data)
                    ws=wb.get_sheet(0)
                    k=table.cell_value(i,3)
                    k=k-120
                    wb.save("Toll_Tax.xls")
                    if(k<0):
                        print("Not Sufficient Balance In Account. Pls Make Payment By Cash")
                    else:
                        ws.write(i,3,k)
                        send_a_command(0x01); 
                        send_a_character(0x0c);
                        send_a_character(0x50);
                        send_a_character(0x61);
                        send_a_character(0x79);
                        send_a_character(0x3a);
                        send_a_character(0x31);
                        send_a_character(0x32);
                        send_a_character(0x30);
                        time.sleep(5)
                elif(ch==2):
                    print("Your Fare Is 200")
                    wb=copy(data)
                    ws=wb.get_sheet(0)
                    k=table.cell_value(i,3)
                    k=k-200
                    wb.save("Toll_Tax.xls")
                    if(k<0):
                        print("Not Sufficient Balance In Account. Pls Make Payment By Cash")
                    else:
                        ws.write(i,3,k)
                        send_a_command(0x01); 
                        send_a_character(0x0c);
                        send_a_character(0x50);
                        send_a_character(0x61);
                        send_a_character(0x79);
                        send_a_character(0x3a);
                        send_a_character(0x32);
                        send_a_character(0x30);
                        send_a_character(0x30);
                        time.sleep(5)
                elif(ch==3):
                    print("Your Fare Is 150")
                    wb=copy(data)
                    ws=wb.get_sheet(0)
                    k=table.cell_value(i,3)
                    k=k-150
                    wb.save("Toll_Tax.xls")
                    if(k<0):
                        print("Not Sufficient Balance In Account. Pls Make Payment By Cash")
                    else:
                        ws.write(i,3,k)
                        send_a_command(0x01); 
                        send_a_character(0x0c);
                        send_a_character(0x50);
                        send_a_character(0x61);
                        send_a_character(0x79);
                        send_a_character(0x3a);
                        send_a_character(0x31);
                        send_a_character(0x35);
                        send_a_character(0x30);
                        time.sleep(5)
            elif(ask==2):
                ch=int(input("Chooose your Vehicle type from above list (1-3) : \n"))
                if(ch==1):
                    print("Your Fare Is 200")
                    wb=copy(data)
                    ws=wb.get_sheet(0)
                    k=table.cell_value(i,3)
                    k=k-200
                    wb.save("Toll_Tax.xls")
                    if(k<0):
                        print("Not Sufficient Balance In Account. Pls Make Payment By Cash")
                    else:
                        ws.write(i,3,k)
                        ws.write(i,4,"yes")
                        send_a_command(0x01); 
                        send_a_character(0x0c);
                        send_a_character(0x50);
                        send_a_character(0x61);
                        send_a_character(0x79);
                        send_a_character(0x3a);
                        send_a_character(0x32);
                        send_a_character(0x30);
                        send_a_character(0x30);
                        time.sleep(5)
                elif(ch==2):
                    print("Your Fare Is 350")
                    wb=copy(data)
                    ws=wb.get_sheet(0)
                    k=table.cell_value(i,3)
                    k=k-350
                    wb.save("Toll_Tax.xls")
                    if(k<0):
                        print("Not Sufficient Balance In Account. Pls Make Payment By Cash")
                    else:
                        ws.write(i,3,k)
                        ws.write(i,4,"yes")
                        send_a_command(0x01); 
                        send_a_character(0x0c);
                        send_a_character(0x50);
                        send_a_character(0x61);
                        send_a_character(0x79);
                        send_a_character(0x3a);
                        send_a_character(0x33);
                        send_a_character(0x35);
                        send_a_character(0x30);
                        time.sleep(5)
                elif(ch==3):
                    print("Your Fare Is 250")
                    wb=copy(data)
                    ws=wb.get_sheet(0)
                    k=table.cell_value(i,3)
                    k=k-250
                    wb.save("Toll_Tax.xls")
                    if(k<0):
                        print("Not Sufficient Balance In Account. Pls Make Payment By Cash")
                    else:
                        ws.write(i,3,k)
                        ws.write(i,4,"yes")
                        send_a_command(0x01); 
                        send_a_character(0x0c);
                        send_a_character(0x50);
                        send_a_character(0x61);
                        send_a_character(0x79);
                        send_a_character(0x3a);
                        send_a_character(0x32);
                        send_a_character(0x35);
                        send_a_character(0x30);
                        time.sleep(5)
            
