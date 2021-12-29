import numpy as np
import matplotlib.pyplot as plt
figure(figsize=(10, 8), dpi=120)

SIVS = open('F4470821.tka', 'r')
# oś Y, liczba zliczeń - num
num = SIVS.read().splitlines()
# Dwa pierwsze indexy to czas pomiaru
Y = num[2:]
Y = [int(x) for x in Y]

Lenght = len(Y)
# print(Lenght)

# oś X
X1 = range(1, Lenght+1)
X = [*X1]
# print(X)

plt.plot(X, Y)
plt.xlabel('Energia [keV]')
plt.ylabel('Liczba zliczeń N')

axY = np.arange(min(Y), max(Y), 20)
plt.yticks(axY)

plt.title('Materiał referencyjny')
plt.fill_between(X, Y)
plt.savefig('mat_ref.png', dpi=150, transparent = True)
plt.show()
