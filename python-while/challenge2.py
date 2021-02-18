# Write the code to implement an improved number guessing game
import random
number = 0
rand_numb = 0
count = 0
print('Guess a number between 1 and 5: ')
while True:
    aux = input( 'Enter guess %d: '% (count + 1))
    if aux.isnumeric() != True:
        print('Numbers only, please!')
        count += 1
        continue
    number = int(aux)
    rand_numb = random.randint(1,5)
    count += 1
    if number == rand_numb:
        print(f'You guessed the number in {count} tries!')
        break
    elif number > rand_numb:
        print('You guess is too high, try again!')
    else:
        print('You guess is too low, try again!')

# You could also initialize the random number before the while statement and do...

number = 0
rand_numb = random.randint(1,5)
count = 0
while number != rand_numb:
    aux = input( 'Enter guess %d: '% (count + 1))
    if aux.isnumeric() != True:
        print('Numbers only, please!')
        count += 1
        continue
    number = int(aux)
    if number > rand_numb:
        print('You guess is too high, try again!')
    elif number < rand_numb:
        print('You guess is too low, try again!')
    count += 1
else:
    print(f'You guessed the number in {count} tries!')