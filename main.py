import numpy as np

# Исходная матрица игры
payoffs = [[8, 8, 6, 7, 8],
           [7, 7, 6, 4, 9],
           [10, 8, 9, 10, 8],
           [3, 6, 9, -2, 8],
           [7, 9, 9, 7, 10]]

print('Исходная матрица игры:')
print(np.array([[8, 8, 6, 7, 8],
                    [7, 7, 6, 4, 9],
                    [10, 8, 9, 10, 8],
                    [3, 6, 9, -2, 8],
                    [7, 9, 9, 7, 10]]))

# Функция для критерия Бернулли
def bernoulli_criterion(payoffs):
    optimal_strategies = [] # Создаем пустой список для оптимальных стратегий

    print("Оптимальные стратегии по критерию Бернулли:")
    for j in range(len(payoffs[0])):
        column_values = [row[j] for row in payoffs] # Получаем все значения из столбца j
        max_payoff = max(column_values) # Находим максимальное значение в столбце
        optimal_strategies.append(max_payoff) # Добавляем максимальное значение в список оптимальных стратегий
        print(f"Максимальное значение в столбце {j+1}: {max_payoff}")

    print("Оптимальные стратегии для каждого столбца:")
    print(optimal_strategies) # Выводим список оптимальных стратегий
    return optimal_strategies

# Функция для критерия Вальда
def wald_criterion(payoffs):
    optimal_strategies = [] # Создаем пустой список для оптимальных стратегий

    print("Оптимальные стратегии по критерию Вальда:")
    for i, row in enumerate(payoffs):
        min_payoff = min(row) # Находим минимальное значение в строке
        optimal_strategies.append(min_payoff) # Добавляем минимальное значение в список оптимальных стратегий
        print(f"Минимальное значение в строке {i+1}: {min_payoff}")

    print("Оптимальные стратегии для каждой строки:")
    print(optimal_strategies) # Выводим список оптимальных стратегий
    return optimal_strategies

# Функция для критерия максимума (оптимистический)
def optimistic_criterion(payoffs):
    transposed_payoffs = list(zip(*payoffs)) # Транспонируем матрицу
    optimal_strategies = [] # Создаем пустой список для оптимальных стратегий

    print("Оптимальные стратегии по критерию максимума (оптимистический):")
    for col in transposed_payoffs:
        max_payoff = max(col) # Находим максимальное значение в столбце
        optimal_strategies.append(max_payoff) # Добавляем максимальное значение в список оптимальных стратегий
        print(f"Максимальное значение в столбце: {max_payoff}")

    print("Оптимальные стратегии для каждого столбца:")
    print(optimal_strategies) # Выводим список оптимальных стратегий
    return optimal_strategies

# Функция для критерия Гурвица
def hurwicz_criterion(payoffs, alpha):
    optimal_strategies = [] # Создаем пустой список для оптимальных стратегий

    print(f"Оптимальные стратегии по критерию Гурвица (α = {alpha}):")
    for i, row in enumerate(payoffs):
        max_payoff = max(row) # Находим максимальное значение в строке
        min_payoff = min(row) # Находим минимальное значение в строке
        hurwicz_value = alpha * max_payoff + (1 - alpha) * min_payoff # Вычисляем значение Гурвица
        optimal_strategies.append(hurwicz_value) # Добавляем значение Гурвица в список оптимальных стратегий
        print(f"Значение Гурвица для строки {i+1}: {hurwicz_value}")

    max_hurwicz_value = max(optimal_strategies) # Находим максимальное значение Гурвица среди всех строк
    print("Максимальное значение Гурвица:")
    print(max_hurwicz_value) # Выводим максимальное значение Гурвица

    return max_hurwicz_value

# Функция для критерия Севиджа
def savage_criterion(payoffs):
    optimal_strategies = [] # Создаем пустой список для оптимальных стратегий

    print("Оптимальные стратегии по критерию Севиджа:")
    for j in range(len(payoffs[0])):
        column = [row[j] for row in payoffs] # Получаем столбец матрицы
        max_value = max(column) # Находим максимальное значение в столбце
        differences = [max_value - value for value in column] # Вычисляем разницу между максимальным значением и каждым элементом
        max_difference = max(differences) # Находим максимальную разницу
        optimal_strategies.append(max_difference) # Добавляем максимальную разницу в список оптимальных стратегий
        print(f"Максимальная разница для столбца {j+1}: {max_difference}")

    min_max_difference = min(optimal_strategies) # Находим минимальную максимальную разницу среди всех столбцов
    print("Минимальная максимальная разница:")
    print(min_max_difference) # Выводим минимальную максимальную разницу

    return min_max_difference

# Вычисляем оптимальные стратегии для каждого критерия
print('\n*** Функция для критерия Бернулли ***')
bernoulli_criterion(payoffs)

print('\n*** Функция для критерия Вальда ***')
wald_criterion(payoffs)

print('\n*** Функция для критерия максимума (оптимистический) ***')
optimistic_criterion(payoffs)

print('\n*** Функция для критерия Гурвица ***')
alpha = 0.5 # Вызываем функцию для критерия Гурвица с заданным коэффициентом оптимизма
hurwicz_criterion(payoffs, alpha)

print('\n*** Функция для критерия Севиджа ***')
savage_criterion(payoffs)
