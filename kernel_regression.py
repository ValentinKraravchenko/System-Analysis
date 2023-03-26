import matplotlib.pyplot as plt
import numpy as np
import openpyxl


def get_kernel_regression_estimation(y, h):
    sse = 10000
    approximated_y = []
    while sse > 1000:
        for i in range(len(y)):
            w = [(1/np.sqrt(2*np.pi)) * np.exp((-1/2)*(((i+1)-j)/h)**2) for j in range(1, len(y))]
            approximated_y.append(sum(list(map(lambda w_value, y_value: w_value*y_value, w, y))) / sum(w))
        sse = sum([(y[i] - approximated_y[i])**2 for i in range(len(y))])

        y = approximated_y[:]
        approximated_y = []
    return y


if __name__ == '__main__':
    wb = openpyxl.load_workbook('gold.xlsx')
    current_sheet = wb.sheetnames[0]
    rows_numbers = int(wb.worksheets[0].dimensions[4:]) + 1
    x_data = [wb[current_sheet][f'A{i}'].value for i in range(2, rows_numbers)][::-1]
    y_data = [wb[current_sheet][f'B{i}'].value for i in range(2, rows_numbers)][::-1]
    x_form = [0, ]
    for i in range(1, len(x_data)):
        x_form.append(x_form[-1] + abs((x_data[i] - x_data[i - 1]).days))
    y_data = list(map(lambda value: value+(0.7*np.random.normal()), y_data))
    windows = [3, 5, 1]
    approximation_results = [get_kernel_regression_estimation(y_data, window_width)
                             for window_width in windows]
    fig, ax = plt.subplots()
    ax.set_title('Gold')
    ax.set_xlabel('Дни')
    ax.set_ylabel('Рубль/Грамм')
    ax.grid()
    ax.plot(x_form, y_data)
    ax.plot(x_form, approximation_results[0])
    ax.plot(x_form, approximation_results[1])
    ax.plot(x_form, approximation_results[2])
    ax.legend(('Исходный ВР с шумом',
               f'h1 = {windows[0]}',
               f'h2 = {windows[1]}',
               f'h3 = {windows[2]}'))
    plt.show()
  
