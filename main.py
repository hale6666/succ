import os
import RPi.GPIO as GPIO
import api
import serial
from time import sleep
import rvm

os.system('modprobe wire timeout=1 slave_ttl=5')
os.system('modprobe w1-gpio')
os.system('modprobe w1-smem')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_slaves')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_remove')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_search')
base_dir = '/sys/devices/w1_bus_master1/w1_master_slaves'
delete_dir = '/sys/devices/w1_bus_master1/w1_master_remove'

"""
def read_rfid():
    id = ""
    print("Ready for RFID tag.")
    rfid.reset_input_buffer()
    read = rfid.read()
    if 'x02' in str(read):
        for i in range(12):
            read = rfid.read()
            id = id + str(read)[2]
        return id
"""

def read_ib():
    f = open(base_dir, "r")
    ID = f.read()
    f.close()
    if ID != 'not found.\n':
        d = open(delete_dir, "w")
        d.write(ID)
        return ID

def insert_mode():
    ib = read_ib()
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
