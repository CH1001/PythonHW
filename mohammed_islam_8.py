# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 05:17:53 2018

@author: Mohammed Islam
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.tile(np.linspace(0,1,1000),(1000,1))
j = np.linspace(-0.4,-0.6,5)
temp = []
temp2 = []
for i in j:
    y = np.tile(np.linspace(i,i+1,1000),(1000,1)).T
    temp.append(y)
     
for m in range(1,6):
    r = np.sqrt((x)**2 + (temp[m-1])**2)
    temp2.append(r)

a = 0
for n in range(1,6):
    a += np.sin(400*temp2[n-1])

plt.figure(1)
plt.imshow(a ,cmap ='gray')
plt.plot(0,400,'r+')
plt.plot(0,450,'r+')
plt.plot(0,500,'r+')
plt.plot(0,550,'r+')
plt.plot(0,600,'r+')

################################################################

j = np.linspace(-0.45,-0.55,50)
temp = []
temp2 = []
for i in j:
    y = np.tile(np.linspace(i,i+1,1000),(1000,1)).T
    temp.append(y)
     
for m in range(1,51):
    r = np.sqrt((x)**2 + (temp[m-1])**2)
    temp2.append(r)

a = 0
for n in range(1,51):
    a += np.sin(3200*temp2[n-1])
    
plt.figure(2)
plt.imshow(a ,cmap ='gray')
# Having a relatively smaller wavelength in comparison to the aperature,
# let the beam stay the same thickness without widening.

################################################################

j = np.linspace(-0.2,-0.8,5)
k = [-0.3,-0.04,0,-0.04,-0.3]
temp = []
temp2 = []
temp3 = []
for i in j:
    y = np.tile(np.linspace(i,i+1,1000),(1000,1)).T
    temp.append(y)
for l in k:
    x = np.tile(np.linspace(l,l+1,1000),(1000,1))
    temp3.append(x)
     
for m in range(1,6):
    r = np.sqrt((temp3[m-1])**2 + (temp[m-1])**2)
    temp2.append(r)

a = 0
for n in range(1,6):
    a += np.sin(900*temp2[n-1])
    
plt.figure(3)
plt.imshow(a ,cmap ='gray')
plt.plot(300,200,'r+')
plt.plot(40,350,'r+')
plt.plot(0,500,'r+')
plt.plot(40,650,'r+')
plt.plot(300,800,'r+')
plt.plot(300,500,'bo')

# Having the sources be in an arc of a circle,
# had the focal point be at the center

################################################################

x = np.tile(np.linspace(0,1,1000),(1000,1))
j = np.linspace(-0.45,-0.55,100)
temp = []
temp2 = []
for i in j:
    y = np.tile(np.linspace(i,i+1,1000),(1000,1)).T
    temp.append(y)
     
for m in range(1,101):
    r = np.sqrt((x)**2 + (temp[m-1])**2)
    temp2.append(r)

a = 0
pi = np.pi
h = int(input('Enter angle in degrees: '))
q = h * (pi/180)
phaseShift = np.sin(q)
for n in range(1,101):
    a += np.sin(3200*temp2[n-1] + phaseShift*(n-1))
    
plt.figure(4)
plt.imshow(a ,cmap ='gray')

# The relationship between the phase shift and the angle shift is,
# the distance b/w each source times sin(angle)