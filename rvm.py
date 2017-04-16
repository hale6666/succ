import serial
import RPi.GPIO as GPIO
from time import sleep
import requests
import json
import api
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT) #Motor Controller Port
GPIO.setup(15, GPIO.OUT) #Motor Controller Port
GPIO.setup(16, GPIO.OUT) #RFID Port
GPIO.setup(18, GPIO.OUT) #RFID Port
GPIO.output(16,False)
GPIO.output(18,False)
rfid = serial.Serial('/dev/ttyAMA0', 9600)

def forward(x):
    GPIO.output(13, GPIO.HIGH)
    sleep(x)
    GPIO.output(13, GPIO.LOW)

def reverse(x):
    GPIO.output(15, GPIO.HIGH)
    sleep(x)
    GPIO.output(15, GPIO.LOW)

def check(inp):
    if inp in st:
        forward(5)
        inserted += 1
    else:
        reverse(5)

def read_rfid():
    id = ""
    read = rfid.read()
    if read == "\x02":
        for i in range(12):
            read = rfid.read()
            id = id + str(read)
            serial.reset_input_buffer()
        return id

def make_list():
    fl = open("barcodes.txt")
    global st
    st = {line for line in fl}
    fl.close()


#ib = read_rfid()
#uid = api.ibutton2uid(ib)
#print(api.getcredits(uid))
def start():
    make_list()
    inp = ""
    while inp != "0":
        inp = input()
        check(inp)
        global inserted = 0
    return inserted

GPIO.cleanup()
