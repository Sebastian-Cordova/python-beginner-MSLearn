# Let us be quiet clear about loops in lists
cities = ['Lima', 'La Paz', 'Caracas', 'Bogota', 'New York']
for city in cities: #the variable city takes the actual element in the list until finish it
    print(city)

# Break out of a for loop
for city in cities:
    if city == 'Bogota':
        cities.append('Moscow') # We can do wathever we want
        break

# Use an else statement
import random # Just for this example put the 'import' function here
numbers = []
for i in range(6): #A list of six elements
    numbers.append(random.randint(1,10)) # We can't use numbers[index] = random.randint(1,10) porque tenemos una lista vacia sin elementos(no podemos contarlos)

for number in numbers:
    if number > 8:
        print('You almost find a number greater than 8')
        break
else:
    print("All the numbers of your list are lower than 8")

# Use a continue statement
for number in numbers: #We are gonna printing just the odd numbers
    if number % 2 == 0:
        continue
    else:
        print(number)
else:
    print('Mission completed') #After the loop we ensure the requirements

# Create nested for loops
names = ['Sebastian', 'Juan', 'Steven', 'Ruben', 'Carlos']
last_names = ['Cordova', 'Orellana', 'Bendezu', 'Quijano', 'Lino']
for name in names:
    for last_name in last_names:
        print(name, last_name)

# Choose randomly from a list
numbers = []
for i in range(10):
    numbers.append(random.randint(1,10))

choiced_number = random.choice(numbers)
print(choiced_number)
choiced_numbers = random.choices(numbers, k = 5)
print(choiced_numbers)

