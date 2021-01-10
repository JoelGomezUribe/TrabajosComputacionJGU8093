from random import *
import matplotlib.pyplot as plt
print("Programas de Probabilidad")
print("Joel  Gómez  Uribe")
print("10 de Enero del 2021")
print("1) Hacer una grafica del valor al que converge la probabilidad de tirar una modena N veces. Hay un resultado para aguila y uno para sol.")
N = []
A = []
S = []
r = 0
n = 20
for i in range(n):
    N.append(i+1)
    r = r + int(2*random())
    A.append(r/(i+1))
    S.append(1-r/(i+1))
plt.plot(N, A,".")
plt.plot(N, S,".")
plt.hlines(.5,0,n)
plt.title("Probabilidad de una moneda")
plt.xlabel("N")
plt.ylabel("Probabilidad")
plt.show()

print("2) Hacer una grafica del valor al que converge la probabilidad de sacar un 3 al tirar un dado de 6 caras N veces")
N = []
D = []
r = 0
q = 0
n = 3
for i in range(n):
    N.append(i+1)
    r = int(6*random()) +1
    if r == 3:
        q = q +1
    D.append(q/(i+1))
plt.plot(N, D,".")
plt.hlines(1/6,0,n)
plt.title("Probabilidad de un dado")
plt.xlabel("N")
plt.ylabel("Probabilidad")
plt.show()

print("3) Hacer una grafica del valor al que converge la probabilidad de sacar un obtener 8 sumado de tirar 2 dados de 6 caras N veces")
N = []
D = []
r = 0
q = 0
n = 3
for i in range(n):
    N.append(i+1)
    r = int(6*random()) +1
    r = r + int(6*random()) +1
    if r == 8:
        q = q +1
    D.append(q/(i+1))
plt.plot(N, D,".")
plt.hlines(5/36,0,n)
plt.title("Probabilidad de dos dados")
plt.xlabel("N")
plt.ylabel("Probabilidad")
plt.show()