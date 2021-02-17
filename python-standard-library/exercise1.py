import random as alias # Using as in the import function we can give an alias to the module to simplify the understanding of our code.
# We can also use any name replacing alias, for example 'dice'
# import random
roll = alias.randint(1, 10) #This function will return a random value between [1, 10]
print(f'The random value is {roll}')

