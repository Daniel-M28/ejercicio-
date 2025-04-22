#Ejercicio 7
#Mayor de Dos Números:
#Pide dos números al usuario. 
#Imprime cuál es el mayor. Si son iguales, indícalo.

try:
  numero1 = int(input('ingresa numero 1: '))
  
  numero2 = int(input('ingresa numero 2: '))
  
  if numero1 > numero2:
      print('numero 1 es mayor')
  
  elif numero2 > numero1:
      print ('numero 2 es mayor')
  
  elif numero2 == numero1:
      print('numeros iguales')

except ValueError:
    print ("ingresa un número válido")