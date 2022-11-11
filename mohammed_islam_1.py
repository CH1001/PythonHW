# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:37:11 2018

@author: Mohammed Islam
"""

import numpy as np
import matplotlib.pyplot as plt
plt.clf
# Figure on slide 7
pi=np.pi
plt.figure(1)
#first plot for the original 2hz sine wave
a=0.01
t=np.arange(0,2,a)
y=np.sin(4*pi*t)*2
ax=plt.subplot(2,2,1)
ax.set_title('Original 2Hz sine wave')
plt.plot(t,y)
#second plot for 2hz sine wave sampled at 5hz
a=0.2
t=np.arange(0,2,a)
y=np.sin(4*pi*t)*2
ax=plt.subplot(2,2,2)
ax.set_title('Sampled')
plt.stem(t,y)
#third plot for discretized plot
a=0.01
t=np.arange(0,2,a)
y=np.sin(4*pi*t)*2
c=np.round(y)
ax=plt.subplot(2,2,3)
ax.set_title('Discretized')
plt.plot(t,c)
#fourth plot thats discretized and sampled
ax=plt.subplot(2,2,4)
ax.set_title('Sampled and Discretized')
a=0.2
t=np.arange(0,2,a)
y=np.sin(4*pi*t)*2
plt.stem(t,y)
a=0.01
t=np.arange(0,2,a)
y=np.sin(4*pi*t)*2
plt.plot(t,y)

# Figure on slide 8
plt.figure(2)
# import a square 256x256 image from directory
P=plt.imread('penny.jpeg').copy()
P=np.mean(P,2) #flattens the image down to 1 dimension without color
# 2 gray levels
L=len(P)
twogray = []
for y in range(L):
    twogray.append([])
    for x in range(L):
        if P[y,x] < 128:
            twogray[y].append(0)
        else:
            twogray[y].append(255)
# 4 gray levels
fourgray = []
for y in range(L):
    fourgray.append([])
    for x in range(L):
        for z in range(1,5):
            if P[y,x] <= (z+1)*256/4:
                fourgray[y].append(z*256/4)
                break
# 8 gray levels
eightgray = []
for y in range(L):
    eightgray.append([])
    for x in range(L):
        for z in range(1,9):
            if P[y,x] <= (z+1)*256/8:
                eightgray[y].append(z*256/8)
                break
# 16 gray levels
sixteengray = []
for y in range(L):
    sixteengray.append([])
    for x in range(L):
        for z in range(1,17):
            if P[y,x] <= (z+1)*256/16:
                sixteengray[y].append(z*256/16)
                break
# 32 gray levels
thirtytwogray = []
for y in range(L):
    thirtytwogray.append([])
    for x in range(L):
        for z in range(1,33):
            if P[y,x] <= (z+1)*256/32:
                thirtytwogray[y].append(z*256/32)
                break
# plots all the images
ax=plt.subplot(2,3,1)
plt.axis('off')
ax.set_title('2 gray levels')
plt.imshow(twogray,cmap='gray')
ax=plt.subplot(2,3,2)
plt.axis('off')
ax.set_title('4 gray levels')
plt.imshow(fourgray,cmap='gray')
ax=plt.subplot(2,3,3)
plt.axis('off')
ax.set_title('8 gray levels')
plt.imshow(eightgray,cmap='gray')
ax=plt.subplot(2,3,4)
plt.axis('off')
ax.set_title('16 gray levels')
plt.imshow(sixteengray,cmap='gray')
ax=plt.subplot(2,3,5)
plt.axis('off')
ax.set_title('32 gray levels')
plt.imshow(thirtytwogray,cmap='gray')
ax=plt.subplot(2,3,6)
plt.axis('off')
ax.set_title('256 gray levels')
plt.imshow(P,cmap='gray') #plots the original image with 256 gray levels

# Figure on slide 13
fig=plt.figure(3)
fig.suptitle('sin(x^2 + y^2)')
import numpy as np
import matplotlib.pyplot as plt
plt.clf
x=np.linspace(0,255,720)
x=np.tile(x,(240,1)) #x array is created
y=np.linspace(0,255,240)
y=np.tile(y,(720,1))  
y=y.T #y array is created
r2 = x**2 + y**2
a = np.sin(r2)
plt.axis('off')
plt.imshow(a,cmap='gray')

# Slide 13 showcasing aliasing in the time domain
plt.figure(4)
#original 10Hz sine wave
a=0.01
t=np.arange(0,2,a)
y=np.sin(20*pi*t) 
ax=plt.subplot(3,1,1)
ax.set_title('Original 10Hz sine wave')
plt.axis('off')
plt.plot(t,y)
# sine wave sampled at 2Hz
a=0.5
t=np.arange(0,2,a)
y=np.sin(20*pi*t)
ax=plt.subplot(3,1,2)
ax.set_title('Sampled at 2Hz')
plt.axis('off')
plt.stem(t,y)
# sine wave sampled at 10Hz
a=0.1
t=np.arange(0,2,a)
y=np.sin(20*pi*t)
ax=plt.subplot(3,1,3)
ax.set_title('Sampled at 10Hz')
plt.axis('off')
plt.stem(t,y)
plt.show()