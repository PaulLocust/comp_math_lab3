def trapezoid_rule(func, a, b, n):
    """
    Метод трапеций для численного интегрирования.

    :param func: функция, которую нужно проинтегрировать
    :param a: нижний предел
    :param b: верхний предел
    :param n: количество разбиений
    :return: приближенное значение интеграла
    """
    h = (b - a) / n
    result = (func(a) + func(b)) / 2  # Начальные значения на концах отрезка

    # Суммируем значения функции в серединах трапеций
    for i in range(1, n):
        x = a + i * h
        result += func(x)

    return result * h
