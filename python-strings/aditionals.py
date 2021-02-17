#Kinds of print
#using .format() method
medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions)

#using f-string
name = 'World'
message = f'Hello, {name}.'
print(message)

count = 10
value = 3.14
message = f'Count to {count}.  Multiply by {value}.'
print(message)

#Sebas examples
amigo = 'Juan'
carrera = 'Ingenieria Civil'
wallet = 200
sentence = 'Mi amigo {}, el cual estudia {}, solo tiene {} soles en su billetera debido a que gasto todo comprando chocolates'.format(amigo, carrera, wallet)
print(sentence)