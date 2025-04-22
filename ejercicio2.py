#Ejercicio 2
# Número Positivo o Negativo
#Pide un número al usuario. Di si es positivo, negativo o si es cero.

try:
  numero = int(input('Ingresa un número: '))
  
  if numero < 0 :
      print("el número es negativo")
  
  elif numero == 0 :
      print ("el número es igual a cero")
  
  elif numero > 0 :
      print ('el número es mayor positivo')

except ValueError:
    print("ingresa un número válido")