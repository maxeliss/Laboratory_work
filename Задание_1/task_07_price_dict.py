# 1. Создать словарь с 5 материалами и ценами
price_list = {
    "Древесина": 2500,
    "Сталь": 4500,
    "Бетон": 1800,
    "Стекло": 3200,
    "Пластик": 1200
}
print("Исходный прайс-лист:", price_list)

# 2. Добавить 2 новых материала
price_list["Керамика"] = 2800
price_list["Композит"] = 5300
print("\nПосле добавления двух материалов:", price_list)

# 3. Изменить цену одного (+10%) (например, у "Сталь")
old_price = price_list["Сталь"]
price_list["Сталь"] = round(old_price * 1.10, 2)  # +10%
print(f"\nИзменение цены 'Сталь': {old_price} → {price_list['Сталь']} (+10%)")

# 4. Удалить один материал (например, "Пластик")
deleted = price_list.pop("Пластик")
print(f"Удалён материал: 'Пластик' (цена была {deleted})")

# 5. Рассчитать среднюю цену
prices = price_list.values()  # получаем все цены
average_price = round(sum(prices) / len(prices), 2)

# Вывод итоговой информации
print("\n=== Итоговый прайс-лист ===")
for material, price in price_list.items():
    print(f"{material}: {price} ₽")
print(f"\nСредняя цена материалов: {average_price} ₽")
print(f"Количество материалов в прайс-листе: {len(price_list)}")