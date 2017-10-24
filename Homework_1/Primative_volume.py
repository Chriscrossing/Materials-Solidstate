#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:36:59 2017

@author: chriscrossing
"""

import numpy as np
import matplotlib.pyplot as plt

#fcc
a = 1
a1 = a/2*np.array([1,1,0])
a2 = a/2*np.array([1,0,1])
a3 = a/2*np.array([0,1,1])

V1 = np.linalg.norm(np.dot(a1, np.cross(a2,a3)));
print(V1);

#bcc
A1 = a/2*np.array([1,1,-1])
A2 = a/2*np.array([-1,1,1])
A3 = a/2*np.array([1,-1,1])

V2 = np.linalg.norm(np.dot(A1, np.cross(A2,A3)));
print(V2);


aA1 = np.cross(a3,a2)/V1 
print(aA1)
aA2 = np.cross(a1,a3)/V1 
print(aA2)
aA3 = np.cross(a2,a1)/V1 
print(aA3)

