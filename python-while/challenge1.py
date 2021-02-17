import random
print('Welcome to the Guesser Bot')

count = 0
flag = True
while flag:
    number = input('Guess a number between 1 and 3: ')
    if number.isnumeric() != True:
        print('You entered a wrong value')
        continue
    number = int(number)
    rand_number = random.randint(1,3)
    if number in range(1,3):
        if number == rand_number:
            print(f'You guess the number, {number} is {rand_number}')
            flag = False
    count += 1
else:
    print(f'You tried to guess {count} times')
