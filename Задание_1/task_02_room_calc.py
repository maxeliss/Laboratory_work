# Ввод размеров помещения с клавиатуры
length = float(input("Введите длину помещения (м): "))
width = float(input("Введите ширину помещения (м): "))
height = float(input("Введите высоту помещения (м): "))

# Расчёт геометрических параметров
floor_area = length * width                     # площадь пола, м²
wall_area = 2 * (length + width) * height       # площадь стен (без учёта окон/дверей), м²
volume = length * width * height                # объём помещения, м³

# Стоимость покраски (125 руб/м²)
painting_cost = wall_area * 125                 # рубли

# Округление до 2 знаков
floor_area = round(floor_area, 2)
wall_area = round(wall_area, 2)
volume = round(volume, 2)
painting_cost = round(painting_cost, 2)

# Лаконичный форматированный вывод
print("\n=== Параметры помещения ===")
print(f"Длина:          {length} м")
print(f"Ширина:         {width} м")
print(f"Высота:         {height} м")
print(f"Площадь пола:   {floor_area} м²")
print(f"Площадь стен:   {wall_area} м²")
print(f"Объём:          {volume} м³")
print(f"Стоимость покраски стен: {painting_cost} руб.")