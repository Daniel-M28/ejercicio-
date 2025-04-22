# Año Bisiesto
#Pide un año al usuario. 
# Determina si es bisiesto 
# (es divisible entre 4 y no entre 100,
#  excepto si también es divisible entre 400).


año = int(input('ingresa un año:'))

if año % 4 == 0:
    print('bisiesto')

else:
    print('No es bisiesto')
