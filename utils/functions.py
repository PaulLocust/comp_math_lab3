import math


# Определение всех функций, которые можно интегрировать
def f1(x):
    """ x^2 """
    return x ** 2


def f2(x):
    """ sin(x) """
    return math.sin(x)


def f3(x):
    """ e^x """
    return math.exp(x)


def f4(x):
    """ 1 / x^2 """
    return 1 / x ** 2


def f5(x):
    """ 1 / x """
    return 1 / x


def f6(x):
    """ 1 / sqrt(x) """
    return 1 / math.sqrt(x)


def f7(x):
    """ -2x^3 - 5x^2 + 7x - 13 """
    return -2 * x ** 3 - 5 * x ** 2 + 7 * x - 13


def f8(x):
    """ 10 """
    return 10


def f9(x):
    """ 1 / sqrt(2x - x^2) """
    return 1 / math.sqrt(2 * x - x ** 2)


# Список всех доступных функций
functions = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
