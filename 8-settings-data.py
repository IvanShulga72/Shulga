import numpy as np
import matplotlib.pyplot as plt
# считали данные из файла settings
with open("settings.txt", "r") as set:
    temp = [float(i) for i in set.read().split("\n")]
    print(temp)
# считали данные из файла data, преобразовали в вольты
data_array = np.loadtxt("data.txt", dtype = int)
volts = [int(i)/256*3.3 for i in data_array]
# определяем ось Х как время
x = np.arange(0, temp[1], temp[1]/len(volts))
plt.figure(figsize=(10, 5))
# рисуем график
plt.plot(x, volts, label=r'V(t)')

# равномерно распределённые значения от 0 до 5, с шагом 0.2
t = np.arange(0., 0.0011, 0.0001)
# ставим точки
plt.plot(x, volts, 'v:m', markevery=15)

# текст на графике
summa = max(data_array)
for i in range(len(data_array)):
    if summa == data_array[i]:
        summa = i
        break
summa = int(temp[0]*i*100)/100

plt.text(4, 2.5, r'Время заряда =' + str(summa))
plt.text(4, 2 , r'Время заряда =' + str(6.01 - summa))
plt.xlabel(r'Время, с', fontsize=14)
plt.ylabel(r'Напряжение, В', fontsize=14)
plt.title(r'Процесс заряда и разряда конденсатора в RC-цепочке', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()