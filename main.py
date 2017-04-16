import os
import RPi.GPIO as GPIO
import api
import serial
from time import sleep
import rvm

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT) #RFID Port
GPIO.setup(18, GPIO.OUT) #RFID Port
GPIO.output(16,False)
GPIO.output(18,False)
rfid = serial.Serial('/dev/ttyAMA0', 9600)

def read_rfid():
    id = ""
    print("Ready for RFID tag.")
    read = rfid.read()
    if 'x02' in str(read):
        for i in range(12):
            read = rfid.read()
            id = id + str(read)[2]
        return id

def insert_mode():
    ib = read_rfid()
    rfid.flushInput()
    uid = api.ibutton2uid(ib)
    credits = api.get_credits(uid)
    print(uid, " : ", credits, " credits")
    ins = rvm.start()
    cr = ins * 5
    print("credits earned: ", cr)
    credits = api.give_credits(uid,cr)
    print(uid, " : ", credits, " credits")
    time.sleep(3)
    print("Thank you for using SUCC.")
    time.sleep(3)
    os.system('clear')

while True:
    insert_mode()
