import RPi.GPIO as GPIO
from time import sleep
import requests
import json
import api
 
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
        print("Valid for Return")
        forward(3)
        return 1
    else:
        print("Not Valid for Return")
        reverse(3)
        return 0

def make_list():
    fl = open("barcodes.txt")
    global st
    st = {line.strip() for line in fl}
    fl.close()


def start():
    GPIO.setwarnings(False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    make_list()
    inp = ""
    inserted = 0
    while inp != "0":
        inp = input("Insert Container\n")
        if inp == "0": break
        inserted += check(inp)
    return inserted
