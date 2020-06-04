# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:17:54 2020

@author: Катрина
"""

import random
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
#русскоязычные подписи на графиках
rcParams['font.family']='fantasy'
rcParams['font.fantasy']='Times New Roman'

N=27 #количество абонентов
M=400#"фреймы"
P=[] #массив вероятностей 
T=[] #массив со среднем временем прибывания в буфере
Por=[] #массив с вероятностями порчи сообщения
#формирования массива вероятностей
p=(1/N)/15
P.append(p)
while p<=(1/N):
    p+=((1/N)/15)
    P.append(p)

for i in range(len(P)):
    frem=[] #заявки "падающие" в один слот
    Q=[] #количетсов заявок в системе
    for j in range(M):
        slot=[0 for i in range(N)]  
        #заполнения слотов (заявки приходящие в систему)
        for k in range(N):
            slot[k]=random.choices([1,0], weights=[P[i],1-P[i]])[0]
        Q.append(sum(slot)) #первый элемент массива
        #заполнения массива
        if Q[j-1]>0:
            Q[j]=Q[j-1]-1+sum(slot)
        else:
            Q[j]=sum(slot)
        frem.append(slot)
    s1=np.sum(frem, axis = 0) #сумма по столбцам
    t=sum([i for i in s1 if i>1]) #количество заявок пришедших в слот >1
    T.append((sum(Q)/len(Q))/P[i])
    Por.append(t/sum(s1))
#построение графиков
fig = plt.figure()
ax1 = fig.add_axes([0,1.2,1,1])
ax1.grid(True, color = [0,0,0])
ax1.set_title('Среднее время нахождения в буфере', fontsize = 18)
ax1.plot(P, T, color='blue')
fig.savefig('gr1.png', bbox_inches='tight')

fig1 = plt.figure()
ax2 = fig1.add_axes([0,0,1,1])
ax2.grid(True, color = [0,0,0])
ax2.set_title('Вероятности порчи пакета', fontsize = 18)
ax2.plot(P, Por, color='blue')
fig1.savefig('gr2.png', bbox_inches='tight')


