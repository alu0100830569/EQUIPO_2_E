#!/usr/bin/python
#!encoding: UTF-8
from math import pi
from math import sin
import difdiv
l=[]
s=[]
n=(0, pi/6, pi/3, pi/2)#tomamos cuatro nodos equidistantes en el intervalo (0,pi/2)
l=difdiv.difdiv(n)
print "El polinomio interpolador de Newton en el intervalo (0, pi/2), para los puntos:\nx0=0\nx1=pi/6\nx2=pi/3\nx3=pi/2\nes: "
print "P(x)= (%f) + (%f)*(x-%f) + (%f)*(x-%f)(x-%f) + (%f)*(x-%f)(x-%f)(x-%f)" %(l[0], l[1], n[0], l[2], n[0], n[1], l[3], n[0], n[1], n[2])
print "Que desarrollando es: "
print "P(x)=(%f)x³+(%f)x²+(%f)x+(%f)"%((l[3]),(l[2]-(l[3]*n[0])-(l[3]*n[1])-(l[3]*n[2])),(l[1]-(l[2]*n[0])-(l[2]*n[1])+(l[3]*n[0]*n[1])+(l[3]*n[0]*n[2])+(l[3]*n[1]*n[2])),((l[1]*n[0])-(l[2]*n[0]*n[1])-(l[3]*n[0]*n[1]*n[2])))