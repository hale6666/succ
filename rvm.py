import RPi.GPIO as GPIO
from time import sleep
import requests
import json

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

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
    else:
        reverse(5)

def main():
    fl = open("barcodes.txt")
    st = {line for line in fl}
    inp = ""
    while inp != "0":
        inp = input()
        check(inp)

main()

GPIO.cleanup()
