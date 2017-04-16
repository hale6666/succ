import os
import RPi.GPIO as GPIO
import api
import rvm

def read_rfid():
    id = ""
    read = rfid.read()
    if read == "\x02":
        for i in range(12):
            read = rfid.read()
            id = id + str(read)
            serial.reset_input_buffer()
        return id

def insert_mode():
    ib = read_rfid()
    uid = api.ibutton2uid(ib)
    ins = rvm.start()
    cr = ins * 5
    api.give_credits(uid,cr)

while True:
    insert_mode()
