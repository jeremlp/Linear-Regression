# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:11:06 2020

@author: Jeremy La Porte
Release 1.0
Linear regression of a set of points
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import time

Y = [i+random.random()*i/400 for i in range(50)] # Set of points Y
X = [i for i in range(len(Y))]# Set of points X

#Distance of a point from the line =====
def getScore(a,b):
    Score = 0
    for k in X:
        Score += ((a*k+b) - Y[k])**2
    return Score
#Init loop============================
a,b = -5,min(Y)
count = 0
Score = getScore(a,b)
Score_min = 100
start_time = time.time()
#Find the line with the best score
while b <= max(Y):
    if count == 1000:
        count = 0
        b += 0.001
        a = 0
    a += 0.01
    Score = getScore(a,b)
    count +=1
    if Score < Score_min:
        Score_min = Score
        Tuple = (a,b)
    if Score_min == 0:
        break

#calcul R^2=============================================
mean = np.array(Y).mean()
SCR = sum([(Y[i] - (Tuple[0]*i+Tuple[1]))**2 for i in X])
SCT = sum([(Y[i] - mean)**2 for i in X])
R_2 = 1- (SCR/SCT)
#temps de simulation ============================
temps_simu = (time.time() - start_time)
print('time :',round(temps_simu,2),'s')
#plot ===========================================
plt.ylim(min(Y)-0.5,max(Y)+0.5)
plt.scatter(X,Y)
print(str(round(Tuple[0],3)) + '*x +' + str(round(Tuple[1],3)),'( R^2 = '+str(round(R_2,2)) + ')', Score_min)
plt.plot(X,[Tuple[0]*i+Tuple[1] for i in X],'r')
