import matplotlib.pyplot
import numpy as np

lambda_ = 0.91
t_ob = 0.73
C_1 = 500
C_2 = 700

mu = 1 / t_ob
ro = lambda_ / mu
L_sist = ro / (1 - ro)
L_ob = P_zan = ro
L_och = L_sist - L_ob
p0 = 1 - ro
T_och = L_och / lambda_
T_sist = L_sist / lambda_

ro_list_l = []
L_sist_list_l = []
L_och_list_l = []
p0_list_l = []
P_zan_list_l = []
T_och_list_l = []
T_sist_list_l = []
lambda_values = np.arange(0.85, 1.01, 0.01)
for lambda_cur in lambda_values:
    ro_cur = lambda_cur / mu
    ro_list_l.append(ro_cur)
    L_sist_list_l.append(ro_cur / (1 - ro_cur))
    L_och_list_l.append(ro_cur / (1 - ro_cur) - ro_cur)
    p0_list_l.append(1 - ro_cur)
    P_zan_list_l.append(ro_cur)
    T_och_list_l.append((ro_cur / (1 - ro_cur) - ro_cur) / lambda_cur)
    T_sist_list_l.append((ro_cur / (1 - ro_cur)) / lambda_cur)

matplotlib.pyplot.figure(1)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость интен-сивности нагрузки канала от lambda')
matplotlib.pyplot.xlabel(r'$lambda$')
matplotlib.pyplot.ylabel(r'$ro$')
matplotlib.pyplot.plot(lambda_values, ro_list_l, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(2)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него числа заявок в системе от lambda')
matplotlib.pyplot.xlabel(r'$lambda$')
matplotlib.pyplot.ylabel(r'$L_s$')
matplotlib.pyplot.plot(lambda_values, L_sist_list_l, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(3)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него числа заявок в очереди от lambda')
matplotlib.pyplot.xlabel(r'$lambda$')
matplotlib.pyplot.ylabel(r'$L_o$')
matplotlib.pyplot.plot(lambda_values, L_och_list_l, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(4)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость веро-ятности свободного канала от lambda')
matplotlib.pyplot.xlabel(r'$lambda$')
matplotlib.pyplot.ylabel(r'$p_0$')
matplotlib.pyplot.plot(lambda_values, p0_list_l, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(5)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость веро-ятности занятого канала от lambda')
matplotlib.pyplot.xlabel(r'$lambda$')
matplotlib.pyplot.ylabel(r'$P_z$')
matplotlib.pyplot.plot(lambda_values, P_zan_list_l, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(6)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него времени пребывания заявок в системе от lambda')
matplotlib.pyplot.xlabel(r'$lambda$')
matplotlib.pyplot.ylabel(r'$T_s$')
matplotlib.pyplot.plot(lambda_values, T_sist_list_l, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(7)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него времени пребывания заявок в очереди от lambda')
matplotlib.pyplot.xlabel(r'$lambda$')
matplotlib.pyplot.ylabel(r'$T_o$')
matplotlib.pyplot.plot(lambda_values, T_och_list_l, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

ro_list_mu = []
L_sist_list_mu = []
L_och_list_mu = []
p0_list_mu = []
P_zan_list_mu = []
T_och_list_mu = []
T_sist_list_mu = []
mu_values = np.arange(1, 1.51, 0.01)
for mu_cur in mu_values:
    ro_cur = lambda_ / mu_cur
    ro_list_mu.append(ro_cur)
    L_sist_list_mu.append(ro_cur / (1 - ro_cur))
    L_och_list_mu.append(ro_cur / (1 - ro_cur) - ro_cur)
    p0_list_mu.append(1 - ro_cur)
    P_zan_list_mu.append(ro_cur)
    T_och_list_mu.append((ro_cur / (1 - ro_cur) - ro_cur) / lambda_)
    T_sist_list_mu.append((ro_cur / (1 - ro_cur)) / lambda_)

matplotlib.pyplot.figure(8)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость интен-сивности нагрузки канала от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$ro$')
matplotlib.pyplot.plot(mu_values, ro_list_mu, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(9)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него числа заявок в системе от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$L_s$')
matplotlib.pyplot.plot(mu_values, L_sist_list_mu, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(10)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него числа заявок в очереди от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$L_o$')
matplotlib.pyplot.plot(mu_values, L_och_list_mu, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(11)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость веро-ятности свободного канала от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$p_0$')
matplotlib.pyplot.plot(mu_values, p0_list_mu, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(12)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость веро-ятности занятого канала от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$P_z$')
matplotlib.pyplot.plot(mu_values, P_zan_list_mu, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(13)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него времени пребывания заявок в системе от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$T_s$')
matplotlib.pyplot.plot(mu_values, T_sist_list_mu, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.figure(14)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него времени пребывания заявок в очереди от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$T_o$')
matplotlib.pyplot.plot(mu_values, T_och_list_mu, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

I = (C_1 * ((1 - ro * np.exp(-(mu-lambda_) * 24)) - (1 - ro * np.exp(-(mu-lambda_) * 12)))
     + C_2 * (1 - (1 - ro * np.exp(-(mu-lambda_) * 24)))) * L_och
print(I)

I_list = []
flag = True
for mu_cur in mu_values:
    ro_cur = lambda_ / mu_cur
    L_och_cur = ro_cur / (1 - ro_cur) - ro_cur
    I_cur = (C_1 * ((1 - ro_cur * np.exp(-(mu_cur-lambda_) * 24)) - (1 - ro_cur * np.exp(-(mu_cur-lambda_) * 12)))
             + C_2 * (1 - (1 - ro_cur * np.exp(-(mu_cur-lambda_) * 24)))) * L_och_cur
    I_list.append(I_cur)
    if I_cur <= 300 and flag:
        flag = False
        print(mu_cur)

matplotlib.pyplot.figure(15)
matplotlib.pyplot.get_current_fig_manager().set_window_title('Зависимость сред-него размера штрафов в сутки от mu')
matplotlib.pyplot.xlabel(r'$mu$')
matplotlib.pyplot.ylabel(r'$I$')
matplotlib.pyplot.plot(mu_values, I_list, 'b', linewidth=1.0)
matplotlib.pyplot.grid()

matplotlib.pyplot.show()
