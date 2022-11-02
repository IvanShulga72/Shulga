#График (точки из файла)
'''
x5=[]
y5=[]
with open('Vn ~ n', 'r') as file:
    arr=file.readlines()
    for line in arr:
        arrx, arry = line.split()
        x5.append(float(arrx))
        y5.append(float(arry))
'''
x3=[]
y3=[]
with open('u^2 ~ F', 'r') as file:
    arr=file.readlines()
    for line in arr:
        arrx, arry = line.split()
        x3.append(float(arrx))
        y3.append(float(arry))
import matplotlib.pyplot as plt
import numpy as np

#Рисование крестов и другое
fig, ax = plt.subplots()
ax.set_title('w ~ m')
ax.set_xlabel('m')
ax.set_ylabel('w')
ax.grid(True, linestyle='-.')
ax.tick_params(labelsize='medium', width=3)
'''
yerr5=[]
for i in y5:
    yerr5.append(0.002*i+0.01)
ax.errorbar(x5, y5, yerr5, fmt='.', linewidth=2, capsize=6, color='k')
'''
yerr3=[]
for i in y3:
    yerr3.append(0.007*i+0.001)
ax.errorbar(x3, y3, yerr3, fmt='.', linewidth=2, capsize=6, color='k')

#Апроксимация
from scipy.optimize import curve_fit
def mapping(x, a, b):
    return a * x + b
'''
args, covar = curve_fit(mapping, x5, y5)
a5 = args[0]
b5 = args[1]
xx5=[]
yy5=[]
for i in range(1500):
    xx5.append(i)
    yy5.append(a5 * i)
plt.plot(xx5, yy5)
print("Значение среднее для :", 1/a5)
print(b5)
'''
args, covar = curve_fit(mapping, x3, y3)
a3 = args[0]
b3 = args[1]
xx3=[]
yy3=[]
for i in range(350):
    xx3.append(i)
    yy3.append(a3 * i + b3)
plt.plot(xx3, yy3)
print("Значение R3:", 1/a3)

plt.show()