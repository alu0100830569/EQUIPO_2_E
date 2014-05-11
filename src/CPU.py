#ecoding: UTF-8
#!/usr/bin/python

import platform
import os

def SOFTinfo():
  infosoft={}
  infosoft={'several':platform.uname() , 'S.O':platform.platform, 'Pythons Version' :platform.python_version(), 'Date' :platform.python_build()}
  
  return infosoft
  
def CPUinfo():
  infofile = '/proc/cpuinfo'
  cpu = {} 
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
	name, value = [w.strip() for w in line.split(':')]
      except:
	continue
      if name == 'model name':
	cpu['CPU type'] = value
      elif name == 'cache size':
	cpu['cache size'] = value
      elif name == 'cpu MHz':
	cpu['CPU speed'] = value + ' Hz '
      elif name == 'vendor_id':
	cpu['vendor ID'] = value
    f.close()
  return cpu
    
if __name__ == '__main__':
  softinfo = SOFTinfo()
  for keys in softinfo.keys():
    print softinfo[keys]
  cpuinfo = CPUinfo()
  for keys in cpuinfo.keys(): #los devuelve las claves del directorio y despues lo usamos como indice
    print cpuinfo[keys]

  print"Introduzca el nombre del fichero en el que desea almacenar los resultados:"
  nombre_fichero = raw_input ();
  f = open(nombre_fichero,"w")
  for keys in softinfo.keys():
    if type (softinfo[keys])is list:
      f.write('\n'.join(softinfo[keys]))
    else: 
      f.write(str(softinfo[keys]))
      f.write('\n')
  for keys in cpuinfo.keys():
    if type (cpuinfo[keys]) is list:
      f.write('\n'.join(cpuinfo[keys]))
    else:
      f.write(str(cpuinfo[keys]))
      f.write('\n')
  f.close()