import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Визначаємо диференціальне рівняння для зростання популяції
def population_model(N, t, beta, delta, p):
    return beta * N**2 / (1 + N) - delta * N - p * N**2

# Коефіцієнти, задані в завданні
beta = 11.2  # коефіцієнт народжуваності
delta = 1.6  # коефіцієнт смертності
p = 4        # внутрішньовидова конкуренція

# Точки часу для симуляції
t = np.linspace(0, 50, 500)  # Розширений час для деталізованішого перегляду

# Визначення початкових умов на основі вимог завдання
lower_critical_limit = 0.4  # раніше розрахована нижня точка рівноваги
upper_critical_limit = 1.0  # раніше розрахована верхня точка рівноваги

initial_conditions = {
    'a': lower_critical_limit / 2 * 0.99,  # трохи менше, ніж половина нижньої межі
    'b': lower_critical_limit / 2 * 1.01,  # трохи більше, ніж половина нижньої межі
    'c': lower_critical_limit,             # точно нижня межа
    'd1': (upper_critical_limit + lower_critical_limit) / 4,   # менше, ніж середнє
    'd2': (3 * upper_critical_limit + lower_critical_limit) / 4, # більше, ніж середнє
    'e': upper_critical_limit,             # точно верхня межа
    'f': upper_critical_limit * 1.01       # трохи більше, ніж верхня межа
}

# Розв'язання диференціального рівняння для кожної початкової умови
solution = {}
for key, N0 in initial_conditions.items():
    solution[key] = odeint(population_model, N0, t, args=(beta, delta, p))

# Малюємо результати для кожного сценарію початкових умов
plt.figure(figsize=(18, 12))
for idx, (key, sol) in enumerate(solution.items(), 1):
    plt.subplot(4, 2, idx)
    plt.plot(t, sol, label=f'Умова {key}')
    plt.title(f'Динаміка за початковою умовою {key}')
    plt.xlabel('Час')
    plt.ylabel('Розмір популяції (N)')
    plt.legend()
    plt.grid(True)

# Вивід критичних точок та висновків у консоль
print(f'Нижня критична межа (рівновага): {lower_critical_limit}')
print(f'Верхня критична межа (рівновага): {upper_critical_limit}')
for key, sol in solution.items():
    final_size = sol[-1, 0]
    conclusion = 'стабілізується в точці рівноваги.' if np.isclose(final_size, lower_critical_limit, atol=0.1) or np.isclose(final_size, upper_critical_limit, atol=0.1) else 'не стабілізується в точці рівноваги.'
    print(f'Початкова умова {key}: Популяція {conclusion}')

plt.tight_layout()
plt.show()
