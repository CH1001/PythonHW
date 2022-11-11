# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:24:09 2018

@author: Mohammed Islam

Lab Group with Eric Luu and Taehyuk Kim
"""

import numpy as np
import matplotlib.pyplot as plt

Step = np.loadtxt('Step_Input_2.txt',usecols=(3)) #Load Step Input
Step1 = np.diff(Step)
fs = 200000 #Sampling Rate
y = np.loadtxt('Step_response_2.txt',usecols=(3)) #Load Step Response
y1 = np.diff(y) #Impulse Response

ep = []
temp = []
avg = np.zeros(67)

#Finding the range of every period
for i in range(1,999):
    if Step1[i] > Step1[i+1] and Step1[i] > Step1[i-1] and Step1[i] > 0.05:
        ep.append(i)
        
#Averaging all the impulse responses        
for j in range(14):
    temp.append(y1[ep[j]:ep[j+1]])
    for k in range(len(temp[j])):
        avg[k]=avg[k]+temp[j][k]
avg = avg/14

#Plotting Code
x = np.linspace(0,67,67)
x = x/fs
plt.plot(x,avg)
#Error Bar on every point using standard deviation
plt.errorbar(x,avg, yerr=np.std(avg))
plt.xlabel('Time (s)')
plt.ylabel('dV/dT (V/s)')