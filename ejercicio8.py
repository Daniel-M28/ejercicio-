#Ejercicio 8
#Clasificación de IMC
#Pide al usuario su peso (kg) y altura (m). 
# Calcula su IMC (peso / altura²) y muestra:

    #"Bajo peso" si es menor a 18.5
    #"Normal" si está entre 18.5 y 24.9
    #"Sobrepeso" si está entre 25 y 29.9
    #"Obesidad" si es mayor o igual a 30

try:

  peso = float(input('ingresa tu peso en Kg: '))
  
  altura = float(input ('ingresa tu altura en m: '))
  
  IMC = peso/(altura**2)
  
  if IMC < 18.5:
      print('Bajo de peso')
  
  elif IMC >= 18.5 and IMC <= 24.9:
      print('Peso normal')
  
  elif IMC >= 25 and IMC <= 29.9:
     print('Sobrepeso')
  
  elif IMC >= 30:
      print ('Obesidad')

except ValueError:
   print("Ingresa un numero correcto")
