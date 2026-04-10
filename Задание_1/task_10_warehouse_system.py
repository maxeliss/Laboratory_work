# Исходные данные
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

# Вывод заголовка таблицы
print("---")
print("СИСТЕМА УЧЁТА СКЛАДА")
print("---")
print(f"{'Материал':<10} | {'Кол-во':<6} | {'Цена':<8} | {'Мин.':<4} | {'Стоимость':<10}")
print("---")

# Переменные для расчётов
total_cost = 0
critical_items = []
max_item_name = ""
max_item_cost = 0

# Проход по всем материалам
for name, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    min_qty = data["min_quantity"]
    cost = quantity * price
    total_cost += cost

    # Определяем самый дорогой материал по общей стоимости
    if cost > max_item_cost:
        max_item_cost = cost
        max_item_name = name

    # Отметка критического остатка
    critical_mark = ""
    if quantity < min_qty:
        critical_mark = " ⚠ КРИТИЧ!"
        critical_items.append((name, quantity, min_qty))

    # Вывод строки таблицы
    print(f"{name:<10} | {quantity:<6} | {price:<8.2f} | {min_qty:<4} | {cost:<10.2f}{critical_mark}")

print("---")
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб\n")

# Самый дорогой материал
print(f"Самый дорогой: {max_item_name} ({max_item_cost:.2f} руб)\n")

# Критические остатки
print(f"⚠ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
for name, qty, min_qty in critical_items:
    print(f"- {name}: {qty} < {min_qty}")

# Выдача материала
print("\n=== ВЫДАЧА МАТЕРИАЛА ===")
material_to_issue = "Цемент"
issue_qty = 25

if material_to_issue in warehouse:
    old_qty = warehouse[material_to_issue]["quantity"]
    if old_qty >= issue_qty:
        new_qty = old_qty - issue_qty
        warehouse[material_to_issue]["quantity"] = new_qty
        print(f"✓ Выдано {issue_qty} единиц '{material_to_issue}'")
        print(f"Остаток: {old_qty} → {new_qty}")
    else:
        print(f"Ошибка: недостаточно {material_to_issue} (есть {old_qty}, требуется {issue_qty})")
else:
    print(f"Материал '{material_to_issue}' не найден")