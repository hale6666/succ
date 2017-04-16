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
        rfid.reset_input_buffer()
        return id

def insert_mode():
    ib = read_rfid()
    rfid.reset_input_buffer()
    uid = api.ibutton2uid(ib)
    credits = api.get_credits(uid)
    print(uid, " : ", credits, " credits")
    ins = rvm.start()
    cr = ins * 5
    print("credits earned: ", cr)
    credits = api.give_credits(uid,cr)['data']
    print(uid, " : ", credits, " credits")
    sleep(3)
    print("Thank you for using SUCC.")
    sleep(3)
    os.system('clear')
    ib = ""

while True:
    insert_mode()
