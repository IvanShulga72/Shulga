import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
[GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW) for i in dac]
[GPIO.setup(i, GPIO.OUT, initial = GPIO.LOW) for i in leds] # Настройка на выход
def led(num): 
    for i in range(8): 
        if i*16 <= num <= (i+1)*16: 
            for j in range(i):
                GPIO.output(leds[j], 1)

def binary(a):
    return [int(i) for i in bin(a)[2::].zfill(8)]
def abc():
    sum = 0
    for i in range(1, 9):
        array = binary(int(256 / 2**i + sum))
        GPIO.output(dac, array)
        time.sleep(0.01)
        compvolt = GPIO.input(comp)
        if (compvolt) == 1:
            sum += int(256 / 2**i) 
    return sum
try:
    while True:
        num = abc()
        if num > 0:
            print(num, int(3.3 * num / 256 * 100) / 100)
        led(num) #вызов включения ледс

finally:
    [GPIO.output(i, 0) for i in dac]
    [GPIO.output(i, 0) for i in leds] # Выключение
    GPIO.cleanup()