#Ejercicio 1 
#Mayor de Edad
#Pide al usuario su edad.
#Si tiene 18 años o más, imprime "Eres mayor de edad". Si no, imprime "Eres menor de edad"

try: 
   edad = int(input('Cual es tu edad? '))
   if edad >= 18:
     print('Eres mayor de edad')
   else:   
     print('Eres menor de edad') 

except ValueError:
     print("Error Ingresa un número válido.")



