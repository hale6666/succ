import os
import RPi.GPIO as GPIO
import api
import rvm

def ibutton_read():
    base_dir = "/sys/devices/w1_bus_master1/w1_master_slaves"
    delete_dir = "/sys/devices/w1_bus_master1/w1_master_remove"
    while True:
        in_data = open(base_dir, "r")
        ib = in_data.read()
        ib_st = ib.strip()
        in_data.close()
        del = open(delete_dir, "w")
        del.write(ib_st)
        del.flush()
        return ib_st

def insert_mode():
    ib = ibutton_read()
    uid = api.ibutton2uid(ib)
    ins = rvm.start()
    cr = ins * 5
    api.give_credits(uid,cr)

while True:
    insert_mode()
