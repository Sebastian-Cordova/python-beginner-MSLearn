first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

#Valores originales
print(first_value)
print(second_value)
print(third_value)

#Valores modificados-> solucion

# First challenge
print(f"\t{first_value.strip().title()}")

# Second challenge
print(f"{second_value.strip('-').strip().capitalize()}")

# Third challenge
#print(f'{third_value:>20}') Esa combinacion de :>valor indica la cantidad de espacios totales en la palabra
cadena_aux = third_value.split(' ')
new_string = ''
for palabra in cadena_aux:
    new_string = new_string + palabra
new_string = new_string.replace('-', ' ').title()
print("\t\t{}".format(new_string))


# Fourth challenge - use only the print() function (no f-strings)
#I've already use a combination of both ways of solution
print("{}#{}#{}!".format(fourth_value,fifth_value,sixth_value))
#Another way to do this challenge
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f"\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}")