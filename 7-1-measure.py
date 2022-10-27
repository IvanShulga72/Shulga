import RPi.GPIO as GPIO
import time
from matplotlib import pyplot as plt

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
    sum = 0
    for i in range(1, 9):
        array = binary(int(256 / 2**i + sum))
        GPIO.output(dac, array)
        time.sleep(0.02)
        compvolt = GPIO.input(comp)
        if (compvolt) == 1:
            sum += int(256 / 2**i) 
    return sum
try:
    mas=[]
    t0 = time.time()
    num = abc()
    count=0
# начало зарядки конденсатора
    print("начало зарядки конденсатора")
    while num < 256*0.97:
        num = abc()
        if num > 0:
            print(num, int(3.3 * num / 256 * 100) / 100)
            mas.append(str(num))
            count+=1
# выставление 0 наряжение на тройка модуле
    print("выставление 0 наряжение на тройка модуле")
    GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
# разрядка кондесатора
    print("разрядка кондесатора")
    while num > 256*0.02:
        num = abc()
        if num > 0:
            print(num, int(3.3 * num / 256 * 100) / 100)
            mas.append(str(num))
            count+=1
# время эксперимента
    t_exp=time.time()-t0
    x=[i * t_exp / count for i in range(1, count + 1)]
    print("Общее время эксперимента", t_exp)
    print("Период одного измерения", t_exp / count)
    print("Средняя частота дискритицации", count / t_exp)
    print("Шаг квантования", 3.3 / 256)
# построение графика
    plt.plot(x, mas)
    plt.show()
# перенос данных в фаил
    set = [str(3.3 / 256), str(count / t_exp)]
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(mas))
    with open("settings.txt", "w") as outfile:
        outfile.write("\n".join(set))

finally:
    print(time.time() - t0)
    [GPIO.output(i, 0) for i in dac]
    GPIO.cleanup()