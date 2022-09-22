import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) 
GPIO.setup(2, GPIO.OUT) 

def binary(a):
    return [int(i) for i in bin(a)[2::].zfill(8)]

try:
    while True:


finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.claenup()