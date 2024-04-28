import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Диференціальне рівняння для зростання популяції мишей
def mouse_population_model(N, t):
    return -0.008 * N**2 + 0.8 * N

# Розрахунок рівноважного розміру популяції (де dN/dt = 0)
def calculate_equilibrium():
    # -0.008 * N^2 + 0.8 * N = 0
    # N(-0.008 * N + 0.8) = 0, N = 0 або N = 100
    return 100  # Тільки позитивне, ненульове рівноважне значення

# Початкові умови: 20 мишей та 180 мишей
initial_conditions = {
    '20_mice': 20,
    '180_mice': 180
}

# Точки часу для симуляції до 12 місяців
t_long_term = np.linspace(0, 12, 300)

# Розв'язуємо диференціальне рівняння для кожної початкової умови на довгий термін
long_term_solution = {}
for key in initial_conditions:
    N0 = initial_conditions[key]
    long_term_solution[key] = odeint(mouse_population_model, N0, t_long_term)

# Знаходимо популяцію на т = 6 місяців для обох початкових умов
t_specific = 6
population_at_6_months = {}
for key in initial_conditions:
    N0 = initial_conditions[key]
    population_at_6_months[key] = odeint(mouse_population_model, N0, [0, t_specific])[-1][0]

# Вивід популяції за 6 місяців до консолі
print(f"Популяція на т = 6 місяців для 20 мишей: {population_at_6_months['20_mice']}")
print(f"Популяція на т = 6 місяців для 180 мишей: {population_at_6_months['180_mice']}")

# Визначення рівноважного розміру популяції
equilibrium = calculate_equilibrium()

# Додатковий аналіз на кінець періоду симуляції
for key, solution in long_term_solution.items():
    final_population = solution[-1][0]
    if final_population > equilibrium:
        status = 'перевищує межу ємності.'
    elif final_population < equilibrium:
        status = 'нижче межі ємності.'
    else:
        status = 'стабілізується на межі ємності.'
    print(f"Кінцева популяція для {key} після 12 місяців {status}")

# Малюємо результати для обох сценаріїв
plt.figure(figsize=(12, 8))
for key in long_term_solution:
    plt.plot(t_long_term, long_term_solution[key], label=f'Початкова умова: {key}')
    plt.axhline(y=equilibrium, color='red', linestyle='--', label='Рівноважна популяція' if key == '20_mice' else None)
plt.title('Динаміка популяції мишей з плином часу')
plt.xlabel('Час (місяці)')
plt.ylabel('Розмір популяції мишей (N)')
plt.legend()
plt.grid(True)
plt.show()
