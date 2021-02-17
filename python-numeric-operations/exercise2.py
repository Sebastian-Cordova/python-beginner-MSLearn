#Determinar si una cadena se puede convertir en un número
#Primer intento(con falla)
first_value = int(input('Ingrese el primer numero:'))
second_value = int(input('Ingrese el segundo valor'))
suma = first_value + second_value
print(f"La suma de valores da como resultado {suma}")
print('La suma de %d y %d da como resultado %d' %(first_value, second_value, suma))
#Hasta este punto, las dos ultimas impresiones(opcionales) estan bien, pero si..
print('Suma = '+str(sum))#Nos da un error al querer cambiar a string el numero
#Esto sucede porque no sabemos si el usuario nos va a pasar un numero o una letra, cuyo caso seria incorrecto



#El error del programa esta basado en una cuestion de programacion conductiva, debemos asumir como programadores el peor escenario posible
value1 = input('Enter the first value:')
if value1.isnumeric() == False:
    print('Value is not a number')
    exit() #Nos permite terminar el programa instantaneamente

value2 = input('Enter the second value:')
if value2.isnumeric() == False:
    print('Value is not a number')
    exit()

suma = int(value1) + int(value2)
print('Suma = ', str(suma))#Ya nos aseguramos de asegurar que los valores sean numeros

#Ponemos ambas condiciones en una sola
value1 = input('Enter the first value:')
value2 = input('Enter the second value:')
if value1.isnumeric() == False or value2.isnumeric() == False:
    print('Value is not a number')
    exit() #Nos permite terminar el programa instantaneamente
#Continuamos con la suma...