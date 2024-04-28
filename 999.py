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

# Початкові популяції двох видів
initial_populations = [10, 5]  # N1 і N2

# Часові точки
t_points = np.linspace(0, 100, 1000)

# Розв'язуємо систему Лотки-Вольтерри
solutions = odeint(lotka_volterra_system, initial_populations, t_points,
                   args=(epsilon1, gamma11, gamma12, epsilon2, gamma21, gamma22))

# Малюємо результати
plt.figure(figsize=(16, 8))

# Малюємо динаміку кожної популяції в часі
plt.subplot(1, 2, 1)
plt.plot(t_points, solutions[:, 0], label='Популяція жертв $N_1$')
plt.plot(t_points, solutions[:, 1], label='Популяція хижаків $N_2$')
plt.title('Часова динаміка популяцій')
plt.xlabel('Час')
plt.ylabel('Розмір популяції')
plt.legend()

# Створюємо фазовий портрет
plt.subplot(1, 2, 2)
plt.plot(solutions[:, 0], solutions[:, 1], label='Фазова траєкторія')
plt.title('Фазовий портрет')
plt.xlabel('Популяція жертв $N_1$')
plt.ylabel('Популяція хижаків $N_2$')
plt.legend()

# Відмічаємо точки рівноваги
equilibrium_N1 = epsilon1 / gamma11
equilibrium_N2 = epsilon2 / gamma22
plt.plot(equilibrium_N1, equilibrium_N2, 'ro', label='Точка рівноваги')

plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Додаткові деталі про динаміку в конкретних часових точках
start_pop = solutions[0]
mid_pop = solutions[len(solutions)//2]
end_pop = solutions[-1]

print("Початкові розміри популяцій: Жертви =", start_pop[0], "Хижаки =", start_pop[1])
print("Розміри популяцій у середині симуляції: Жертви =", mid_pop[0], "Хижаки =", mid_pop[1])
print("Розміри популяцій на кінці симуляції: Жертви =", end_pop[0], "Хижаки =", end_pop[1])
