# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:25:48 2018

@author: Mohammed Islam
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
plt.clf
plt.figure(1) #replicating original slide
fs, x = wav.read('speech.wav') #importing wav file
a = np.linspace(0,len(x)/fs,len(x)) #adjusting x axis to be in seconds
plt.subplot(3,1,1)
X = x/len(x)
plt.plot(a,X)
plt.xlabel('t in seconds')
plt.ylabel('f(t)')
s=np.fft.fft(X) #fourier transform
plt.subplot(3,1,2)
b = np.linspace(0,fs,len(x))
plt.plot(b,abs(s)) # plotting frequency
plt.xlim(0,fs/2) # cutting off at Nyquist frequency
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.subplot(3,1,3)
angle = np.angle(s)
plt.plot(b,angle) # plotting angle
plt.xlim(0,fs/2)
plt.xlabel('Frequency')
plt.ylabel('Angle')

plt.figure(2) # alteration of slide
pi = np.pi
y = np.sin(2000*pi*a)*0.03 # 1 kHz sine wave
n = X + y # added to the original sound wave
plt.subplot(3,1,1)
plt.plot(a,n)
plt.xlabel('t in seconds')
plt.ylabel('f(t)')
S=np.fft.fft(n) # fourier transform
plt.subplot(3,1,2)
plt.plot(b,abs(S)) # plotting freqeuncy
plt.xlim(0,fs/2)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.subplot(3,1,3)
angle2 = np.angle(S) # plotting angle
plt.plot(b,angle2)
plt.xlim(0,fs/2)
plt.xlabel('Frequency')
plt.ylabel('Angle')