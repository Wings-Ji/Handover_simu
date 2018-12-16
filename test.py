# -*- coding: utf-8 -*-
# @Time    : 18/6/25 下午 9:51
# @Author  : Ji
# @File    : test.py
# @Software: PyCharm
import handover
import matplotlib.pyplot as plt
import numpy as np

hdtimesset,simltset,pptset,pre_pptset, timeset = handover.run(5001,0.3)
# for runtm in range(1000,5000,555):
#     handovertimes,simulttime,pingpangtimes,pre_pingpangtimes = handover.run(runtm,0.9)
#     hdtimesset.append(handovertimes)
#     simltset.append(simulttime)
#     pptset.append(pingpangtimes)
#     pre_pptset.append(pre_pingpangtimes)
#     print(handovertimes,simulttime,pingpangtimes,pre_pingpangtimes)

# x_c = range(1000,5000,555)
# plt.plot(timeset,hdtimesset,marker = '*',label='traditional HO')
# plt.plot(timeset,np.array(hdtimesset)-np.array(pptset)+np.array(pre_pptset),
#          marker = 'h',label = 'proposed HO')
plt.plot(timeset,pptset,marker = '^',label ='traditional pingpang HO')
plt.plot(timeset,pre_pptset,marker = 'p',label = 'proposed pingpang HO')
plt.ylim(0,130)
plt.xlabel('SimulationTime(t)(in secs)')
plt.ylabel('Number of pingpang-handovers')
plt.legend(loc=2,fontsize = 9)
# plt.grid()
plt.show()
