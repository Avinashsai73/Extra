# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:51:21 2022

@author: avina
"""
# load libraries
import pandas as pd
import os
import math
import numpy as np

n = 0.020 # coeffficient
h = 5  # ft
angle = 45 # degree
z = 3 # % in slope
L = 1 # mile

# Define function
def manning(q,n,A,R,S):
    Q = 1500 #Cfs
    Q = ((1.49/n)*A*R*np.power(1.6)*np.squar*S)
    return (Q)
print ()

n = 0.020 # coeffficient
h = 5  # ft
angle = 45 # degree
z = 3 # % in slope
L = 1 # mile

#find the area
A = ((1/2)*z*1)*2
print (A)

# find the 




