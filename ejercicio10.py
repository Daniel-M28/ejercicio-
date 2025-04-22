#Ejercicio 10
#Pide un número al usuario.  
#Di si está dentro del rango de 1 a 10 (inclusive). 

try:

  numero = int(input ('ingresa un numero: '))
  
  if 1 <= numero <= 10:
     print("número dentro del rango")
  
  else:
     print("numero fuera del rango")

except ValueError:
 print("ingresa un numero correcto")
