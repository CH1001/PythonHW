# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 06:43:16 2021

@author: Mohammed Islam
"""

import numpy as np

def charge():
#----------Inputs-and-Conversions----------#
    E = input("E = ")
    E = float(E)
    fall = input("avg fall time = ")
    fall = float(fall)
    rise = input("avg rise time = ")
    rise = float(rise)
    nsm = input("n = ")
    nsm = float(nsm)
    press = input("p = ")
    press = float(press)
#-----------Variable-Calculations----------#
    V = E*0.01 
    p = press * 1000
    n = nsm * 0.00001
    vf = 0.0001 / fall
    vr = 0.0001 / rise
    b = 0.0082
    c = (4 * np.pi)/3
    g = 9.8
    P = 886
    d = 0.0001
#----------------Formula-------------------#
    a = (b/(2*p))
    x = (9*n*vf)/(2*P*g)
    sqrt = np.sqrt(a**2 + x)
    f = (P*g*d*(vf + vr))/(V*vf)
    q = c*((sqrt - a)**3)*f
    print(q)