# Ввод цены и количества товара
price = float(input("Введите цену за единицу товара (₽): "))
quantity = int(input("Введите количество товара: "))

# Расчёт начальной стоимости
initial_cost = price * quantity

# Определение скидки в зависимости от суммы
if initial_cost < 1000:
    discount_percent = 0
elif 1000 <= initial_cost <= 5000:
    discount_percent = 5
else:  # > 5000
    discount_percent = 10

# Расчёт суммы скидки и итоговой стоимости
discount_amount = initial_cost * discount_percent / 100
final_cost = initial_cost - discount_amount

# Округление до 2 знаков (для денежных сумм)
initial_cost = round(initial_cost, 2)
discount_amount = round(discount_amount, 2)
final_cost = round(final_cost, 2)

# Вывод всех этапов расчёта
print("\n=== Калькулятор скидки ===")
print(f"Цена за единицу: {price} ₽")
print(f"Количество: {quantity} шт.")
print(f"Начальная стоимость: {initial_cost} ₽")
print(f"Размер скидки: {discount_percent}%")
print(f"Сумма скидки: {discount_amount} ₽")
print(f"Итоговая стоимость: {final_cost} ₽")