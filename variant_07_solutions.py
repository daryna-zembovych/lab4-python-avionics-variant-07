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
    ...

# Задача 3: Нагнітання тиску (while / else)
def charge_pressure_vessel(target_bar: float) -> str:
    """
    У циклі while збільшує тиск на 1.5 бар.
    Якщо тиск перевищує 60 бар -> аварійний break ("Аварійне скидання").
    Якщо досягнуто target_bar штатно -> через else повертає "Розрахунковий тиск досягнуто успішно".
    """
    ...

# Задача 4: Тасування координат (range / slicing)
def process_trajectory_shifts(coords: list) -> list:
    """
    Для кожного i в range(len(coords)) здійснює зсув списку coords[i:] + coords[:i]
    та обчислює відстані між першими двома точками зсунутого списку.
    """
    ...
