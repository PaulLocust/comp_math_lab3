def simpson_rule(func, a, b, n):
    """
    Метод Симпсона для численного интегрирования.

    :param func: функция, которую нужно проинтегрировать
    :param a: нижний предел
    :param b: верхний предел
    :param n: количество разбиений (должно быть чётным)
    :return: приближенное значение интеграла
    """
    if n % 2 != 0:
        raise ValueError("Количество разбиений n должно быть чётным для метода Симпсона.")

    h = (b - a) / n
    result = func(a) + func(b)

    # Суммируем все элементы с коэффициентами
    for i in range(1, n):
        coef = 3 + (-1) ** (i + 1)
        x = a + i * h
        result += coef * func(x)

    return result * h / 3
