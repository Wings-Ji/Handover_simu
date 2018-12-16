# -*- coding: utf-8 -*-
# @Time    : 18/6/26 下午 9:51
# @Author  : Ji
# @File    : plot.py
# @Software: PyCharm
import matplotlib.pyplot as plt

name_list = ['relative ESA                ', 'increase rate of average delay                 ']
traditional = [0.796, 0.402]
proposed = [1, 0.116]
x = list(range(len(traditional)))
total_width, n = 0.6, 2
width = total_width / n

plt.bar(x, traditional, width=width,edgecolor = 'b', linewidth = 1,label='tradition', fc='y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, proposed, width=width, label='proposed',edgecolor = 'b', linewidth = 1, tick_label=name_list, fc='r')
plt.legend()
plt.show()