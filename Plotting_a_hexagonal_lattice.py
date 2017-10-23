#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:33:11 2017

Adapted from examples on this page:
    http://people.exeter.ac.uk/sh481/the-reciprocal-lattice.html
Accessed Wed 18th October 2017.

@author: chriscrossing
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import lines
from Functions import*



rc('text', usetex=True)


# Real space lattice vectors.
a=10
a1=a*np.array([np.sqrt(3)/2,1/2])
a2=a*np.array([np.sqrt(3)/2,-1/2])
v1=a*np.array([np.sqrt(3)/6,0]) #added
v2= -v1 #added


# Vectors orthogonal to a1 and a2 (for labeling)
a1n=np.array([a1[1],-a1[0]])/np.sqrt(np.dot(a1,a1))
a2n=np.array([a2[1],-a2[0]])/np.sqrt(np.dot(a2,a2))

#For the basis (for labeling vectors)
v1n=np.array([v1[1],-v1[0]])/np.sqrt(np.dot(v1,v1))
v2n=np.array([v2[1],-v2[0]])/np.sqrt(np.dot(v2,v2))

#Now plot the real space lattice
# 2N x 2N lattice points
N=4
nv=np.arange(-N,N)
mv=np.arange(-N,N)

# Coordinates of the lattice points
xp=np.array([[i*a1[0]+j*a2[0] for i in nv] for j in mv])
yp=np.array([[i*a1[1]+j*a2[1] for i in nv] for j in mv])

# Coordinates for the Basis
xb = np.array([i+v1[0] for i in xp])
yb = np.array([i+v1[1] for i in yp])
xb2 = np.array([i+v2[0] for i in xp])
yb2 = np.array([i+v2[1] for i in yp])

# Hexagon proof. Need to find 6 points, join them with lines, work out the distance and angle.
#Hexagon point coords
H1 = -1*a2-1*v1
H2 = -1*a1-1*a2+v1
H3 = -1*a1-1*v1
H4 = -1*a1+v1
H5 = -1*v1
H6 = -1*a2+v1

#For the basis (for labeling vectors)
H1n=np.array([H1[1],-H1[0]])/np.sqrt(np.dot(H1,H1))
H2n=np.array([H2[1],-H2[0]])/np.sqrt(np.dot(H2,H2))
H3n=np.array([H3[1],-H3[0]])/np.sqrt(np.dot(H3,H3))
H6n=np.array([H6[1],-H6[0]])/np.sqrt(np.dot(H6,H6))

#Hexagon dx
H2H1 = H2-H1
H3H2 = H3-H2
H4H3 = H4-H3
H5H4 = H5-H4
H6H5 = H6-H5
H1H6 = H1-H6
H6H1 = H6-H1

#Checks distance between hexagon points.
D12 = np.sqrt((H1[0]-H2[0])**2+(H1[1]-H2[1])**2)
D12 = '%.2f' % D12
D23 = np.sqrt((H2[0]-H3[0])**2+(H2[1]-H3[1])**2)
D23 = '%.2f' % D23
D34 = np.sqrt((H3[0]-H4[0])**2+(H3[1]-H4[1])**2)


#Checks angle between 
cosine_angle = np.dot(H2H1, H6H1) / (np.linalg.norm(H6H1) * np.linalg.norm(H2H1)) 
angle = np.arccos(cosine_angle) 
angle_between_H2H1H6 = np.degrees(angle)










# Plot range
xmax=0.5*N*min(np.sqrt(np.dot(a1,a1)),np.sqrt(np.dot(a2,a2)))
# Plot things
plt.plot(xp.flatten(),yp.flatten(),'o')
plt.plot(xb.flatten(),yb.flatten(),'x',color='green')
plt.plot(xb2.flatten(),yb2.flatten(),'x',color='green')


#arrows for Primitave vectors 
plt.arrow(0,0,a1[0],a1[1],color='r',head_width=0.1,length_includes_head=True)
plt.arrow(0,0,a2[0],a2[1],color='r',head_width=0.1,length_includes_head=True)
plt.text(0.5*a1[0]+0.3*a1n[0],0.5*a1[1]+0.3*a1n[1],"$\mathbf{a}_{1}$",fontsize=10)
plt.text(0.5*a2[0]+0.1*a2n[0],0.5*a2[1]+0.1*a2n[1],"$\mathbf{a}_{2}$",fontsize=10)

#arrows for Basis
plt.arrow(0,0,v1[0],v1[1],color='g',head_width=0.1,length_includes_head=True)
plt.arrow(0,0,v2[0],v2[1],color='g',head_width=0.1,length_includes_head=True)
plt.text(0.5*v1[0]+0.3*v1n[0],0.5*v1[1]+0.3*v1n[1],"$\mathbf{v}_{1}$",fontsize=10)
plt.text(0.5*v2[0]+0.1*v2n[0],0.5*v2[1]+0.1*v2n[1],"$\mathbf{v}_{2}$",fontsize=10)

#lines for hexagon
plt.arrow(H1[0],H1[1],H2H1[0],H2H1[1],color='b',head_width=0.1,length_includes_head=True)
plt.arrow(H2[0],H2[1],H3H2[0],H3H2[1],color='b',head_width=0.1,length_includes_head=True)
plt.arrow(H3[0],H3[1],H4H3[0],H4H3[1],color='b',head_width=0.1,length_includes_head=True)
plt.arrow(H4[0],H4[1],H5H4[0],H5H4[1],color='b',head_width=0.1,length_includes_head=True)
plt.arrow(H5[0],H5[1],H6H5[0],H6H5[1],color='b',head_width=0.1,length_includes_head=True)
plt.arrow(H6[0],H6[1],H1H6[0],H1H6[1],color='b',head_width=0.1,length_includes_head=True)

#Line length lables
plt.text(0.5*H1[0]+0.5*H1n[0],0.5*H1[1]+0.3*H1n[1],D12+"a",fontsize=10)

#Angle lables



plt.xlabel("$x$",fontsize=18)
plt.ylabel("$y$",fontsize=18)
plt.xlim(-xmax,xmax)
plt.ylim(-xmax,xmax)
plt.title("Hexagon Lattice",y=1.05)
# The angles of the lines will look wrong if the aspect ratio is not equal
plt.axes().set_aspect('equal')

plt.savefig("Diagram.eps", format='eps', dpi=600);
