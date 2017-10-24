#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:41:35 2017

@author: chriscrossing
"""

import numpy as np
import matplotlib.pyplot as plt
pi = np.pi;
a = 1;


G = 2*pi/a*np.array([1,-2,0])

d1 = 1*pi/np.linalg.norm(G)

k1 = 2*pi/a*np.array([3/2,0,0])

k2 = 2*pi/a*np.array([3/2,2,0])

np.dot(-2*k1,G)