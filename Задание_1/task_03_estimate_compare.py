# 1. Запрашиваем температуру в градусах Цельсия
celsius = float(input("Введите температуру в °C: "))

# 2. Переводим в Фаренгейты по формуле: F = C * 9/5 + 32
fahrenheit = celsius * 9/5 + 32

# 3. Определяем состояние воды
if celsius <= 0:
    state = "Лёд"
elif celsius < 100:   # от 1 до 99 °C
    state = "Жидкость"
else:                 # 100 °C и выше
    state = "Пар"


print(f"{celsius} °C = {fahrenheit:.2f} °F, состояние: {state}")