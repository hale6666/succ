import os
import RPi.GPIO as GPIO
import api
import serial
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT) #RFID Port
GPIO.setup(18, GPIO.OUT) #RFID Port
GPIO.output(16,False)
GPIO.output(18,False)
rfid = serial.Serial('/dev/ttyAMA0', 9600)

def read_rfid():
    id = ""
    read = rfid.read()
    if 'x02' in str(read):
        for i in range(12):
            read = rfid.read()
            id = id + str(read)[2]
        return id

def insert_mode():
    print("ready")
    ib = read_rfid()
    print("ib: ", ib)
    uid = api.ibutton2uid(ib)
    print("uid: ", uid)
    cr = api.get_credits(uid)
    print("credits: ", cr)

insert_mode()

GPIO.cleanup()
