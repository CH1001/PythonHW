# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 00:29:36 2018

@author: Mohammed Islam
"""

import numpy as np
import matplotlib.pyplot as plt

SR = np.loadtxt('Step_Response.txt',usecols=(2))
IR =  np.diff(SR)
FR = np.fft.fft(IR)
Mag = abs(FR)
phase = np.angle(FR)
fs = 10000
fbin = np.linspace(0,fs,len(Mag))
t = np.linspace(0,len(IR),len(IR))
t = t/fs

#Plotting impulse, Magnitude, and Phase Response
plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t,IR)
plt.title('Impulse Response')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.subplot(2,2,2)
plt.plot(fbin,Mag)
plt.title('Magnitude Response')
plt.xlabel('Freq')
plt.ylabel('Gain')
#Plotting points that correlate with the 4 sinusoid inputs
plt.plot(10.000526343491762,35.908463444101145,'ro')
plt.plot(15.263961261119006,3.3328326670981463,'ro')
plt.plot(30.001579030475288,5.733682872012377,'ro')
plt.plot(60.003158060950575,0.4934892860729007,'ro')
plt.xlim(0,fs/2)
plt.subplot(2,2,3)
plt.plot(fbin,phase)
plt.title('Phase Response')
plt.xlabel('Freq')
plt.ylabel('Phase Shift')
#Plotting points that correlate with the 4 sinusoid inputs
plt.plot(10.000526343491762,2.994522897525632,'ro')
plt.plot(15.263961261119006,2.9994163467391948,'ro')
plt.plot(30.001579030475288,0.7591049306165878,'ro')
plt.plot(60.003158060950575,2.27532075532317,'ro')
plt.xlim(0,fs/2)

#Plotting the sinusoids at 4 different frequencies
plt.figure(2)
SinR1 = np.loadtxt('10hz.txt',usecols=(5,2))
SinR2 = np.loadtxt('15hz.txt',usecols=(5,2))
SinR3 = np.loadtxt('30hz.txt',usecols=(5,2))
SinR4 = np.loadtxt('60hz.txt',usecols=(5,2))
t2 = np.linspace(0,len(SinR1),len(SinR1))
t2 = t2/fs
plt.subplot(2,2,1)
plt.plot(t2,SinR1)
plt.title('10 Hz')
plt.xlabel('Time')
plt.ylabel('Voltage')
t3 = np.linspace(0,len(SinR2),len(SinR2))
t3 = t3/fs
plt.subplot(2,2,2)
plt.plot(t3,SinR2)
plt.title('15 Hz')
plt.xlabel('Time')
plt.ylabel('Voltage')
t4 = np.linspace(0,len(SinR3),len(SinR3))
t4 = t4/fs
plt.subplot(2,2,3)
plt.plot(t4,SinR3)
plt.title('30 Hz')
plt.xlabel('Time')
plt.ylabel('Voltage')
t5 = np.linspace(0,len(SinR4),len(SinR4))
t5 = t5/fs
plt.subplot(2,2,4)
plt.plot(t5,SinR4)
plt.title('60 Hz')
plt.xlabel('Time')
plt.ylabel('Voltage')