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
plt.plot(x, volts, label=r'V(t)')
plt.plot(x, volts, 'v:m')
plt.xlabel(r'Время, с', fontsize=14)
plt.ylabel(r'Напряжение, В', fontsize=14)
plt.title(r'Процесс заряда и разряда конденсатора в RC-цепочке', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()