# Шаг 1: подключаем библиотек math для поиска факториала
import math

# Шаг 2: считываем из файла массив чисел через генератор
a = [int(x) for x in open('17-easy.txt')]

# Шаг 3: инициализируем массив для ответа
ans = []

# Шаг 4: запускаем цикл, который будет перебирать подряд идущие тройки чисел
for i in range(len(a) - 2):
    # Шаг 5: переобозначаем числа для удобства как x, y, z
    x, y, z = a[i], a[i + 1], a[i + 2]
    # Шаг 6: считаем факториалы Fy, Fxz
    Fy, Fxz = math.factorial(y), math.factorial(x + z)
    # Шаг 7: проверяем условие
    if Fy > Fxz:
        # Шаг 8: записываем в массив ans Fy
        ans.append(Fy)

# Шаг 9: выводим в ответ кол-во троек (длина массива) и максимальный факториал (максимум массива)
print(len(ans), max(ans))
