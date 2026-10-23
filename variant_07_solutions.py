"""
Лабораторна робота: Варіант 7
Студент: Зембович Дарина
Група: EIP 30
"""

# Задача 1: Розблокування скидання вантажу (розширене розпакування)
def unlock_payload(data_tuple: tuple) -> str:
    """
    Приймає кортеж (status, *codes).
    Якщо status == "ARMED" та сума кодів == 100 -> "Розблоковано",
    інакше -> "Заблоковано".
    """
    (status, *codes) = data_tuple
    if status == "ARMED" and sum(codes) == 100:
        print("Розблоковано")
    else:
        print("Заблоковано")


# Задача 2: Класифікатор цілей радара (match-case)
def classify_radar_target(target: tuple) -> str:
    """
    Приймає (target_type, distance_km, speed_m_s).
    - ("aircraft", d, v) при v > 300 -> "Швидкісний літак на відстані {d} км"
    - ("drone", d, v) при v < 100 -> "Малошвидкісний БПЛА на відстані {d} км"
    - _ -> "Невідомий об'єкт"
    """
    match target:
        case ("aircraft", d, v) if v > 300:
            print(f"Швидкісний літак на відстані {d} км")
        case ("drone", d, v) if v < 100:
            print(f"Малошвидкісний БПЛА на відстані {d} км")
        case _:
            print(f"Невідомий об'єкт")
               

# Задача 3: Нагнітання тиску (while / else)
def charge_pressure_vessel(target_bar: float) -> str:
    """
    У циклі while збільшує тиск на 1.5 бар.
    Якщо тиск перевищує 50 бар -> аварійний break ("Аварійне скидання").
    Якщо досягнуто target_bar штатно -> через else повертає "Розрахунковий тиск досягнуто успішно".
    """
    p = 0.0
    while p <= target_bar:
        if p > 50:
            print("Аварійне скидання")
            break
        p += 1.5
    else:
        print("Розрахунковий тиск досягнуто успішно")


# Задача 4: Тасування координат (range / slicing)
def process_trajectory_shifts(coords: list) -> list:
    """
    Для кожного i в range(len(coords)) здійснює зсув списку coords[i:] + coords[:i]
    та обчислює відстані між першими двома точками зсунутого списку.
    """
    distances = []
    for i in range(len(coords)):
        shifted_coords = coords[i:] + coords[:i]
        point1 = shifted_coords[0]
        point2 = shifted_coords[1]
        d = ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)**0.5
        distances.append(d)
    return distances

#Test 1.1
print('Test 1.1')
unlock_payload(("ARMED", 20, 30, 50))
unlock_payload(("not ARMED", 20, 30, 50))
unlock_payload(("ARMED", 20, 30, 40))

#Test 1.2
print('Test 1.2')
classify_radar_target(("aircraft", 10, 350))
classify_radar_target(("aircraft", 10, 200))
classify_radar_target(("drone", 20, 50))
classify_radar_target(("drone", 20, 150))
classify_radar_target(("plane", 20, 100))

#Test 1.3
print('Test 1.3')
charge_pressure_vessel(50.0)
charge_pressure_vessel(60.0)

#Test 1.4
print('Test 1.4')
print(process_trajectory_shifts([(1, 1), (0, 1), (2, 3), (4, 5)]))