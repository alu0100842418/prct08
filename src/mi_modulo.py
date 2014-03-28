#!/usr/bin/python
PI = 3.1415926535897931159979634685441852
def aprox(n):
  suma = 0
  for i in range (1,n+1):
    xi = (i-0.5)/n
    fxi = 4.0/(1.0 + xi*xi)
    suma += fxi
  pi = float (suma)/n
  return pi

if __name__=="__main__":

    l = []
    veces = int(raw_input('Numero de veces: '))
    while veces <= 0:
	print 'El numero debe ser mayor que 0'
	veces = int(raw_input('Numero de veces: '))
    n = int(raw_input('Numero de intervalos: '))
    while n <= 0:
	print 'El numero debe ser mayor que 0'
	n = int(raw_input('Numero de intervalos: '))
    
    for i in range (1,veces+1):
      a = i * n
      s = aprox(a)
      l = l + [s]
    print l