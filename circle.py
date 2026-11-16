import math


def area(r):
    """
    Вычисляет площадь круга по радиусу r.

        Параметры:
            r (int | float): радиус круга
        
        Возвращаемое значение:
            area (float): площадь круга

        Пример вызова:
            area(2)
    """

    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга по радиусу r.

        Параметры:
            r (int | float): радиус круга

        Возвращаемое значение:
            perimeter (float): периметр круга

        Пример вызова:
            perimeter(2)
    """

    return 2 * math.pi * r

