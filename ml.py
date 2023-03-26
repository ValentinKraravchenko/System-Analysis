import math
import matplotlib.pyplot as plt

x = [1108, 1437, 1217, 1053, 1333, 1909, 1730, 1533, 1862, 1943, 2045, 2151, 2431, 2183, 2069, 2785, 2886, 2557, 2671,
     2532, 3167, 3412, 3048, 3179, 3289]
y = [6.1, 9.1, 7.2, 7.5, 6.9, 11.5, 10.3, 9.5, 9.2, 10.6, 12.5, 12.9, 14.5, 13.6, 12.8, 16.5, 17.1, 15.0, 16.2, 15.8,
     19.0, 19.4, 19.1, 18, 20.2]
x2 = []
xy = []
for ind, val in enumerate(x):
    x2.append(val ** 2)
    xy.append(val * y[ind])
print('x^2 = ', x2)
print('x*y = ', xy)
print('sum(x) = ', sum(x))
print('sum(y) = ', sum(y))
print('sum(x^2) = ', sum(x2))
print('sum(x*y) = ', sum(xy))
x_middle = sum(x) / len(x)
y_middle = sum(y) / len(y)
print('x middle = ', sum(x) / len(x))
print('y middle = ', sum(y) / len(y))

s_x = 0
for val in x:
    s_x += (val - x_middle) ** 2
s_x = math.sqrt(s_x / (len(x) - 1))
s_y = 0
for val in y:
    s_y += (val - y_middle) ** 2
s_y = math.sqrt(s_y / (len(y) - 1))
print('sx = ', s_x)
print('sy = ', s_y)
r_x_y = (sum(xy) - len(x) * y_middle * x_middle) / ((len(x) - 1) * s_x * s_y)
print('rxy = ', r_x_y)

a1 = 0.00595
a0 = 0.00633
y_model = []
for val in x:
    y_model.append(a1 * val + a0)
approx = 0
for ind, val in enumerate(y_model):
    approx += abs(y[ind] - val) / y[ind]
approx = approx / len(y_model) * 100
print('A = ', approx)

f_fact = (0.972 / (1 - 0.972)) * 23
print('f fact = ', f_fact)

s_ost = 0
for ind, val in enumerate(y_model):
    s_ost += (y[ind] - val)**2
s_ost = math.sqrt(s_ost / (len(y_model) - 2))
print('S ost = ', s_ost)

y_model_new = []
for val in x:
    y_model_new.append(a1 * val)
s_ost_new = 0
for ind, val in enumerate(y_model_new):
    s_ost_new += (y[ind] - val)**2
s_ost_new = math.sqrt(s_ost_new / (len(y_model) - 2))
print('S ost new = ', s_ost_new)

s_p = s_ost * math.sqrt(1 + 1 / len(y_model_new) + (2500 - 2221.2)**2 / (25 * 717.775))
print('S p = ', s_p)

plt.get_current_fig_manager().set_window_title('Корреляционное поле и прямая уравнения регрессии')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.plot(x, y_model_new, 'b', linewidth=1)
plt.scatter(x, y, 15, 'r')
plt.show()
