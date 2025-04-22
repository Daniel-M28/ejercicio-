#5. Calculadora de Propinas
#Pide al usuario el total de una cuenta.
#Luego pregunta qué porcentaje de propina 
#quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

try:

  cuenta = float(input('Total de tu cuenta: '))
  
  propina= int(input ('Que porcentaje de propina quieres dejar? 10%, 15%, o 20%?'))
  
  if propina not in [10, 15, 20]:
        print("Por favor ingresa un porcentaje válido: 10, 15 o 20.")
  
  else: 
      
    Valor_propina = cuenta * (propina/100)
  
    total= cuenta + Valor_propina
    
    print(f"el total a pagar es  $: {total}")

except ValueError:
    print("ingresa un valor correcto")