#Ejercicio 6
#Adivina el Número
#Fija un número secreto (por ejemplo, 7).
#Pide al usuario que lo adivine. Di 
#Si su número es mayor, menor o igual al número secreto.

try:
  numero = 5 
  
  intento= int(input('adivina el numero: '))
  
  if intento == 5:
     print('numero adivinado')
  
  elif intento < 5:
     print('el numero es mayor')
  
  elif intento > 5:
     print ('el numero es menor')

except ValueError:
   print("Ingresa un número válido")

