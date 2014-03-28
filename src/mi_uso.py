#/usr/bin/python
import mi_modulo

def error(intervalo, pruebas, umbral):
  fallo=0
  for i in range(1, pruebas+1):
    aprox = mi_modulo.aprox(intervalo)
    error = abs(aprox - mi_modulo.PI)
    if error > umbral:
      fallo += 1
  return (fallo / float(pruebas)) * 100.0
 
if __name__=="__main__":

  intervalo = int (raw_input('Numero de intervalos: '))
  while intervalo <=0:
    print 'El numero de intervalos debe ser mayor que cero'
    intervalo =int(raw_input('Numero de intervalos'))
  
  pruebas = int (raw_input('Numero de pruebas: '))
  while pruebas <=0:
    print 'El numero de pruebas debe ser mayor que cero'
    pruebas =int(raw_input('Numero de pruebas'))
 
  umbral = float (raw_input('Numero del umbral: '))
  while umbral <=0:
    print 'El numero del umbral debe ser mayor que cero'
    umbral =float(raw_input('Numero del umbral: '))
  l = error(intervalo, pruebas, umbral)
  print l