import numpy as np
from numpy import linalg as LA


def normalization(array): ## нормализуем вектор
    temp = np.ones(len(array))
    for i in range(len(array)):
        for j in range(len(array[i])):
            temp[i] *= array[i][j]
        temp[i] = temp[i] ** (1 / len(temp))
    temp = temp / sum(temp)
    return temp


def consistency_check(array, number_c): ## проверка на согласованность
    random_consistency = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
    wa = LA.eigvals(np.array(array))
    lambda_max = round(max(wa.real))
    consistency_index = (lambda_max - len(array)) / (len(array) - 1)
    consistency_relation = consistency_index / random_consistency[len(array)]
    print(f'lambda_max = {lambda_max}')
    print(f'consistency_index = {consistency_index}')
    print(f'consistency_relation = {consistency_relation}')
    if consistency_relation < 0.1:
        print(f'Paired comparison matrix by C {number_c + 1} is consistency')
    else:
        print(f'Paired comparison matrix by C {number_c + 1} is inconsistency')


F = np.array([[6,9,8,7,6], ## вводим исходную матрицу
              [6,2,3,9,9],
              [8,8,5,1,7],
              [7,2,5,7,9],
              [9,2,7,5,4],
              [6,7,6,5,4]])
rating = [2,1,6,4,3] ## весовые критерии
A_long = len(F)
C_long = len(F[0])
AHP = [0] * A_long
AHP_plus = [0] * A_long
C = np.zeros((C_long, C_long))
F_transpose = F.transpose()
mps = np.zeros((A_long, A_long))
E = np.zeros((A_long, A_long))
Pairwise_measurement_matrix = np.zeros((C_long, A_long))

for i in range(C_long): ## МПС для критериев
    for j in range(C_long):
        C[i][j] = rating[i] / rating[j]
normalized_eigenvector_C = normalization(C)

for k in range(C_long): ## МПС альтернатив по всем критериям
    for i in range(A_long):
        for j in range(A_long):
            mps[i][j] = F_transpose[k][i] / F_transpose[k][j]
    print(f'MPS C{k + 1}\n{mps}')
    consistency_check(mps, k)
    Pairwise_measurement_matrix[k] = normalization(mps)
    print(f'Normalized vector:{Pairwise_measurement_matrix[k]}\n')

for i in range(A_long): ## вычисляем итоговый весовой вектор для МАИ
    for j in range(C_long):
        AHP[i] += Pairwise_measurement_matrix[j][i] * normalized_eigenvector_C[j]

print('AHP:')
for i in range(len(AHP)): ## принтую итоговый весовой вектор для МАИ
    print(f'w[{(i + 1)}] = {AHP[i]}')

for i in range(A_long):  ## нахожу вектор E
    for j in range(A_long):
        for k in range(C_long):
            E[i][j] += (Pairwise_measurement_matrix[k][i] / (Pairwise_measurement_matrix[k][i] + Pairwise_measurement_matrix[k][j])) *  normalized_eigenvector_C[k]
print(f'E\n{E}')
for i in range(A_long):  ## вычисляем итоговый весовой вектор для МАИ+
    AHP_plus[i] = sum(E[i])
AHP_plus = AHP_plus/sum(AHP_plus)
print('\nAHP_plus:')
for i in range(len(AHP_plus)): ## принтую итоговый весовой вектор для МАИ+
    print(f'w[{(i + 1)}] = {AHP_plus[i]}')
