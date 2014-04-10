#!/usr/bin/python
#!encoding: UTF-8
from math import pi
from math import sin
#definimos una función, con la que obtendremos el valor de los diferentes notos empleados, en nuestro caso la funcion es el seno(x)
def seno(x):
  f=sin(x)
  return f
  
if __name__=="__main__":#Prueba para la funcion seno(x)
  n=int(raw_input("Introduzca un punto de prueba: "))
  print "El seno de dicha función es: %.3f" %seno(n)
