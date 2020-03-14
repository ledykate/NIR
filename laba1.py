# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:17:54 2020

@author: Катрина
"""

import random
import matplotlib.pyplot as plt
from matplotlib import rcParams
#русскоязычные подписи на графиках
rcParams['font.family']='fantasy'
rcParams['font.fantasy']='Times New Roman'

N=10
M=2000
P=[]
p=(1/N)/20
P.append(p)
T=[]
while p<=(1/N):
    p+=((1/N)/20)
    P.append(p)


for i in range(len(P)):
    #frem=[]
    Q=[]
    for j in range(M):
        slot=[0 for i in range(N)]  
        for k in range(N):
            slot[k]=random.choices([1, 0], weights=[P[i],1-P[i]])[0]
        #s=sum(slot)
        Q.append(sum(slot))
        if Q[j-1]>0:
            Q[j]=Q[j-1]-1+sum(slot)
        else:
            Q[j]=sum(slot)
    T.append((sum(Q)/len(Q))/P[i])

fig = plt.figure()
ax1 = fig.add_axes([0,1.2,1,1])
ax1.grid(True, color = [0,0,0])
#ax1.set_title('График ', fontsize = 18)
ax1.plot(P, T, color='blue')
#fig.savefig('gravic_fun.png', bbox_inches='tight')


