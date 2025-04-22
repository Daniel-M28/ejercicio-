#Ejercicio 3
#Par o Impar
#Pide un número entero. Indica si es par o impar.

try:
  numero = int(input('Ingresa un numero: '))
  if numero % 2 == 0 :
      print('Es un numero par')
  
  else:
      print("Es un numero impar")
      
except ValueError:
     print("Ingresa un número válido")