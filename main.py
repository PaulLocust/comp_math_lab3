import math
from integrators.methods import compute_integral
from utils.discontinuity import get_discontinuity_points
from utils.functions import functions


def try_to_compute(func, x):
    """Попытка вычисления функции в точке с обработкой ошибок."""
    try:
        return func(x)
    except Exception:
        return None


def handle_discontinuities(func, a, b, breakpoints, eps, epsilon, method):
    """
    Обрабатывает разрывы функции и вычисляет интегралы по сегментам, избегая точек разрыва.
    """
    res = 0
    n = 0

    # Проверка первой части от a до первого разрыва
    if try_to_compute(func, a) is not None and try_to_compute(func, breakpoints[0] - eps) is not None:
        result, n1 = compute_integral(func, a, breakpoints[0] - eps, epsilon, method)
        res += result
        n += n1

    # Проверка последней части от последнего разрыва до b
    if try_to_compute(func, b) is not None and try_to_compute(func, breakpoints[0] + eps) is not None:
        result, n1 = compute_integral(func, breakpoints[0] + eps, b, epsilon, method)
        res += result
        n += n1

    # Обработка промежуточных разрывов
    for bi in range(len(breakpoints) - 1):
        b_cur = breakpoints[bi]
        b_next = breakpoints[bi + 1]

        if try_to_compute(func, b_cur + eps) is not None and try_to_compute(func, b_next - eps) is not None:
            result, n1 = compute_integral(func, b_cur + eps, b_next - eps, epsilon, method)
            res += result
            n += n1

    return res, n


if __name__ == "__main__":
    while True:
        # Выбор функции для интегрирования
        print("Выберите функцию для интегрирования:")
        print("1. x^2")
        print("2. sin(x)")
        print("3. e^x")
        print("4. 1/x^2")
        print("5. 1/x")
        print("6. 1/sqrt(x)")
        print("7. -2x^3 - 5x^2 + 7x - 13")
        print("8. 10")
        print("9. 1 / sqrt(2x - x^2)")

        while True:
            try:
                choosen_f = int(input("Ваш выбор: ")) - 1
                if choosen_f < 0 or choosen_f >= len(functions):
                    print("Ошибка: Пожалуйста, выберите номер от 1 до 9.\n")
                    continue  # Если выбор вне диапазона, повторяем запрос
                func = functions[choosen_f]
                break  # Если выбор корректен, выходим из цикла
            except ValueError:
                print("Ошибка: Пожалуйста, введите число.\n")

        # Ввод пределов интегрирования
        while True:
            try:
                a = float(input("Введите начальный предел интегрирования (a): "))
                b = float(input("Введите конечный предел интегрирования (b): "))

                if a >= b:
                    print(f'{a} >= {b}. Пожалуйста, введите a < b')
                else:
                    break
            except ValueError:
                print("Ошибка ввода! Пожалуйста, введите корректные числовые пределы.\n")

        # Проверка на разрывы функции
        breakpoints = get_discontinuity_points(func, a, b, math.ceil(b - a) * 100)

        if len(breakpoints) != 0:
            print(f"Обнаружены точки разрыва: {breakpoints}.")
            eps = 0.00001  # малое значение для корректного вычисления около разрывов
            converges = True

            # Проверка на сходимость функции на разрывах
            for bp in breakpoints:
                y1 = try_to_compute(func, bp - eps)
                y2 = try_to_compute(func, bp + eps)
                if y1 is not None and y2 is not None and abs(y1 - y2) > eps or (y1 == y2 and y1 is not None):
                    converges = False # Не сходится
                    break

            if not converges:
                print('- Интеграл не существует: функция не сходится на разрывах.')
            else:
                print('+ Интеграл существует: функция сходится на разрывах.')

                # Ввод точности и корректировка ввода
                while True:
                    try:
                        epsilon_input = input("Введите требуемую точность вычислений: ")
                        # Заменяем запятую на точку для корректной конверсии
                        epsilon = float(epsilon_input.replace(',', '.'))
                        break
                    except ValueError:
                        print("Ошибка ввода! Пожалуйста, введите корректную числовую точность.\n")

                while True:
                    # Выбор метода интегрирования
                    print("\nВыберите метод интегрирования:")
                    print("1. Метод левых прямоугольников")
                    print("2. Метод правых прямоугольников")
                    print("3. Метод средних прямоугольников")
                    print("4. Метод трапеций")
                    print("5. Метод Симпсона")

                    try:
                        method_choice = int(input("Ваш выбор: "))
                        method_dict = {
                            1: "rectangle_left",
                            2: "rectangle_right",
                            3: "rectangle_middle",
                            4: "trapezoid",
                            5: "simpson"
                        }

                        if method_choice not in method_dict:
                            print("Пожалуйста, выберите корректный метод!")
                            continue

                        method = method_dict[method_choice]
                        print(f"\nМетод: {method}")

                        # Корректировка пределов на основе точек разрыва
                        res, n = handle_discontinuities(func, a, b, breakpoints, eps, epsilon, method)

                        print(f"Значение интеграла: {res}")
                        print(f"Число разбиений для достижения требуемой точности: n = {n}")

                        break  # Прерываем цикл выбора метода после вычисления
                    except ValueError:
                        print("Ошибка: Пожалуйста, введите число.\n")

        else:
            # Если разрывов нет, вычисляем интеграл по обычной формуле
            while True:
                # Ввод точности и корректировка ввода
                try:
                    epsilon_input = input("Введите требуемую точность вычислений: ")
                    # Заменяем запятую на точку для корректной конверсии
                    epsilon = float(epsilon_input.replace(',', '.'))
                    break
                except ValueError:
                    print("Ошибка ввода! Пожалуйста, введите корректную числовую точность.\n")

            while True:
                # Выбор метода интегрирования
                print("\nВыберите метод интегрирования:")
                print("1. Метод левых прямоугольников")
                print("2. Метод правых прямоугольников")
                print("3. Метод средних прямоугольников")
                print("4. Метод трапеций")
                print("5. Метод Симпсона")

                try:
                    method_choice = int(input("Ваш выбор: "))
                    method_dict = {
                        1: "rectangle_left",
                        2: "rectangle_right",
                        3: "rectangle_middle",
                        4: "trapezoid",
                        5: "simpson"
                    }

                    if method_choice not in method_dict:
                        print("Пожалуйста, выберите корректный метод!")
                        continue

                    method = method_dict[method_choice]
                    print(f"\nМетод: {method}")

                    result, n = compute_integral(func, a, b, epsilon, method)

                    if result is not None and n is not None:
                        print(f"Значение интеграла: {result}")
                        print(f"Число разбиений для достижения требуемой точности: n = {n}")

                    break  # Прерываем цикл выбора метода после вычисления
                except ValueError:
                    print("Ошибка: Пожалуйста, введите число.\n")

        # Спрашиваем, продолжить ли выполнение программы
        while True:
            user_input = input('\nХотите попробовать ещё раз? [y/n]: ').lower()
            if user_input == 'y':
                break
            elif user_input == 'n':
                print("Goodbye!")
                exit()  # Завершаем программу
            else:
                print("Некорректный ввод! Пожалуйста, введите 'y' или 'n'.")
