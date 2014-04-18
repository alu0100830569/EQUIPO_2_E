#!/usr/bin/python
#!encoding: UTF-8
from math import pi
from math import sin
import seno
def difdiv(x):
  c=[]#lista que guardará cada una de las diferencias divididas.
  c=c+[0]#ya que la primera diferencia dividida es cero (f(0))
  c1=(seno.seno(x[1])-seno.seno(x[0]))/(x[1]-x[0])
  c=c+[c1]
  c12=(seno.seno(x[2])-seno.seno(x[1]))/(x[2]-x[1])#diferencia divi0, x1, x2, x3dida entre x1 y x2
  c2=(c12-c1)/(x[2]-x[0])
  c=c+[c2]
  c23=((seno.seno(x[3])-seno.seno(x[1]))/(x[3]-x[2]))
  c13=((c23-c12)/(x[3]-x[1]))
  c3=((c13-c2)/(x[3]-x[0]))
  c=c+[c3]
  return c
  
if __name__=="__main__":#Prueba para la funcion difdiv(x)
  x=(0, pi/6, pi/3, pi/2)
  print difdiv(x)
