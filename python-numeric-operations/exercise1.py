#Escribir un código que use la función type() en el archivo de código
print(type('Hola, me llamo Sebastián'))
print(type(69))
print(type(69.69))
#Como pueden observar, cada tipo de dato corresponde a una clase distinta: string, int y float

#La funcion isinstance(): indica si el valor corresponde a la clase adjuntada. Si es, retornara True
print(isinstance('Sebitas', str))#->Si es
print(isinstance('Chucho el perro cobarde', int))

print(isinstance(124, int))#->Si es 
print(isinstance(124, float))

print(isinstance(24.69, float))#->Si es
print(isinstance(24.69, str))

#¿Se puede crear una expresión booleana mediante la función type()?
print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)