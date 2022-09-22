import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
[GPIO.setup(i, GPIO.OUT) for i in dac]

def binary(a):
    return [int(i) for i in bin(a)[2::].zfill(8)]

try:
    while True:
        for i in range(255):
            a = binary(i)
            [GPIO.output(dac[i], a[i]) for i in range(8)] 
            time.sleep(0.01)
        for i in range(255, 1, -1):
            a = binary(i)
            [GPIO.output(dac[i], a[i]) for i in range(8)] 
            time.sleep(0.01)

finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.claenup