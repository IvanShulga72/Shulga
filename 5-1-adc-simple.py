import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
[GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW) for i in dac]
def binary(a):
    return [int(i) for i in bin(a)[2::].zfill(8)]
def abc():
    for i in range(256):
        array = binary(i)
        GPIO.output(dac, array)
        compvolt = GPIO.input(comp)
        time.sleep(0.005)
        if compvolt == 0:
            return i
try:
    while True:
        num = abc()
        if num > 0:
            print(num, int(3.3 * num / 256 * 100) / 100)

finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.cleanup()