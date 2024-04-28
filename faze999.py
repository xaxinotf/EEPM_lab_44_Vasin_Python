import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Визначаємо рівняння Лотки-Вольтерри для двох видів
def lotka_volterra_system(N, t, epsilon1, gamma11, gamma12, epsilon2, gamma21, gamma22):
    N1, N2 = N
    dN1_dt = (epsilon1 - gamma11 * N1 - gamma12 * N2) * N1
    dN2_dt = (-epsilon2 + gamma21 * N1 - gamma22 * N2) * N2
    return [dN1_dt, dN2_dt]

# Припускаємо типові значення коефіцієнтів
epsilon1, gamma11, gamma12 = 0.1, 0.02, 0.02
epsilon2, gamma21, gamma22 = 0.1, 0.02, 0.02

# Функція для обчислення похідних у даній точці (для стрімплоту)
def derivatives(y, x):
    return lotka_volterra_system([y, x], 0, epsilon1, gamma11, gamma12, epsilon2, gamma21, gamma22)

# Створюємо сітку точок
Y, X = np.mgrid[0:4:100j, 0:4:100j]

# Обчислюємо похідні в кожній точці на сітці
U, V = derivatives(Y, X)

# Розв'язуємо систему Лотки-Вольтерри для прикладу траєкторії
t_points = np.linspace(0, 100, 1000)
initial_populations = [2, 2]  # Приклад початкової популяції
trajectory = odeint(lotka_volterra_system, initial_populations, t_points,
                    args=(epsilon1, gamma11, gamma12, epsilon2, gamma21, gamma22))

# Малювання
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, U, V, color='lightgray')  # Стрімплот
plt.plot(trajectory[:, 0], trajectory[:, 1], color='red')  # Приклад траєкторії
plt.xlabel('Популяція жертв $N_1$')
plt.ylabel('Популяція хижаків $N_2$')
plt.title('Фазовий портрет зі стрімплотом')
plt.grid(True)
plt.show()
