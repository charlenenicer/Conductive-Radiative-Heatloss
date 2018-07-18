#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:12:52 2018

@author: charlenenicer
"""
import matplotlib.pyplot as plt
import  numpy as np
# Righthand  side of  differential  equation
#(2.99*10**(-3))


def f(x):
    return  (2.99E-3)*((2.22E-2)*(1)*(5.67E-8)*(293.15**4-x**4)-1.32*(2.22E-2)/(0.0256)**(1/4)*(x-293.15)**(5/4))
# Define  initial  condition
x0 = 356.15
# Time  step
dt = 0.01
# Solve  the  differential  equation  from  time 0 to time T
T = 4800
# Define  discretized  time; assumes  dt  divides  nicely  into T
t = np.linspace(0, T, int(T/dt)+1)
# An  array  to store  the  solution
x = np.zeros(len(t))
# Integrate  the  differential  equation  using  Euler’s method
x[0] = x0
for i in  range(1, len(t)):
    x[i] = x[i-1] + f(x[i -1])* dt
    
# Create a new  figure
plt.figure ()
# Plot  solution
plt.plot(t, x)