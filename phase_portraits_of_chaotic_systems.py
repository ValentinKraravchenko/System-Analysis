import matplotlib.pyplot
import numpy as np


def get_x0():
    while True:
        try:
            num = float(input("Введите начальное значение x (x0): "))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def get_n():
    while True:
        try:
            num = int(input("Введите количество переменных x (n): "))
            if num <= 0:
                print("Вы ввели не натуральное число. Повторите ввод")
                num = get_n()
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def get_r():
    while True:
        try:
            num = float(input("Введите r для определения зависимости x от време-ни и фазовых портретов (от 1 до 4): "))
            if num < 0 or num > 4:
                print("Значение должно находиться в диапазоне от 0 до 4. Повто-рите ввод")
                num = get_r()
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def get_r0():
    while True:
        try:
            num = float(input("Введите r0 для построения бифуркационной диаграм-мы (от 1 до 4): "))
            if num < 0 or num > 4:
                print("Значение должно находиться в диапазоне от 0 до 4. Повто-рите ввод")
                num = get_r0()
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def get_rn(r0):
    while True:
        try:
            num = float(input("Введите rn (кранее правое) для построения бифур-кационной диаграммы (от r0 до 4): "))
            if num < r0 or num > 4:
                print("Значение должно находиться в диапазоне от ", r0, " до 4. Повторите ввод")
                num = get_rn(r0)
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def get_h():
    while True:
        try:
            num = float(input("Введите шаг для построения бифуркационной диа-граммы (h (от 0.0001 до 1)): "))
            if num < 0.0001 or num > 1:
                print("Значение должно находиться в диапазоне от 0.0001 до 1. Повторите ввод")
                num = get_h()
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def get_k():
    while True:
        try:
            num = int(input("Введите количество последних значений x для постро-ения бифуркационной диаграммы (k (от 50 до 500)): "))
            if num < 50 or num > 500:
                print("Значение должно находиться в диапазоне от 50 до 500. По-вторите ввод")
                num = get_k()
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def main():
    # Ввод данных модели с клавиатуры
    x0 = get_x0()
    n = get_n()
    r = get_r()
    r0 = get_r0()
    rn = get_rn(r0)
    h = get_h()
    k = get_k()

    # Инициализация списка значений x
    f = [x0]
    # Инициализация списка значений x + 1 для построения фазового портрета
    x_1 = []
    # Массив моментов времени
    t = [0]
    # Вычисление значений
    for ind in range(1, n, 1):
        f.append(r * f[-1] * (1 - f[-1]))
        x_1.append(f[-1])
        t.append(ind)
    # Построение графика зависимости x от времени
    matplotlib.pyplot.figure(1)
    matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость x от времени')
    matplotlib.pyplot.title('Зависимость x от времени')
    matplotlib.pyplot.xlabel(r'$t$')
    matplotlib.pyplot.ylabel(r'$x$')
    matplotlib.pyplot.plot(t, f, 'r', linewidth=1.0)
    matplotlib.pyplot.grid()
    # Построение фазового портрета
    matplotlib.pyplot.figure(2)
    matplotlib.pyplot.get_current_fig_manager().set_window_title('Фазовый порт-рет')
    matplotlib.pyplot.title('Фазовый портрет')
    matplotlib.pyplot.xlabel(r'$x$')
    matplotlib.pyplot.ylabel(r'$x+1$')
    f.pop()
    matplotlib.pyplot.plot(f, x_1, 'r', linewidth=1.0)
    matplotlib.pyplot.grid()

    # Инициализация списка значений x
    f_r = [x0]
    # Построение бифуркационной диаграммы
    matplotlib.pyplot.figure(3)
    matplotlib.pyplot.get_current_fig_manager().set_window_title('Бифуркационная диаграмма')
    # Вычисление значений
    for r_temp in np.arange(r0, rn + h, h):
        for ind in range(1, n, 1):
            f_r.append(round(r_temp * f_r[-1] * (1 - f_r[-1]), 4))
        f_r = f_r[n-k:n]
        r_mass = [r_temp] * k
        matplotlib.pyplot.plot(r_mass, f_r, color='black', linestyle=' ', marker='.', markersize=1)
    matplotlib.pyplot.title('Диаграмма ветвления при ' + str(r0) + ' <= r <= ' + str(rn))
    matplotlib.pyplot.xlabel(r'$r$')
    matplotlib.pyplot.ylabel(r'$f$')
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
