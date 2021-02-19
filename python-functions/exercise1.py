#My first function
def say_hello():
    print('Hello World!')

#Function with input
def say_hello_2(name):
    print(f'Hello {name}!')

#Function with optional argument
# Al definir un parámetro de entrada como parte de la función, se requiere un argumento. Si se quiere que el argumento sea opcional, 
# se puede proporcionar un valor predeterminado que se usa si el autor de la llamada no pasa un argumento
def say_hello_3(name = 'World'):
    print(f'Hello {name}!')

# Function with a second optional parameter
# Actualizar el ejemplo de código para incluir un segundo parámetro opcional de entrada
def say_hello_4(name='World', greeting=None):
    if greeting == None:
        print(f'Hello {name}!')
    else:
        print(f'{greeting} {name}!')

#Function that returns a value
def add_two_numbers(num1, num2):
    return num1 + num2

#Function that returns a list
def making_love_couples():
    boyz = ['Sebastian', 'Juan', 'Ruben', 'Lino', 'Steven']
    girlz = ['Romina', 'Andrea', 'Milene', 'Brisa', 'Carmen', 'Caroline']
    couples = []
    for boy in boyz:
        for girl in girlz:
            couples.append(f'Probably {boy} get engaged with {girl}')
    return couples

say_hello()
say_hello_2('Sebastian')
say_hello_3()
say_hello_3('Juan')
say_hello_4('Ivan', greeting='Howdy')
say_hello_4('Ivan', 'Howdy')
say_hello_4(greeting='Howdy') #If I dont wanna put the first optional input of the function, we should refer the variable what we want to refer

print(add_two_numbers(10,15))
print(making_love_couples())
print(len(making_love_couples()))