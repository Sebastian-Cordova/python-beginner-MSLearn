#First problem
#We are gonna count how many iterations we need to get a '5' in a 'virtual' dice

import random 
roll = 0
count = 0
while roll != 5:
    roll = random.randint(1,5)
    count += 1
    print(roll)
print(f"It took {count} rolls to roll a '5'")

# Second problem: using break and else in our while
# Take a look: We are able to use an 'else' after a 'while' !!! 
# We are gonna print the person who has roll a '5' in their first attempt and then stop the iteration

roll = 0
count = 0
print("First person to roll a '5' wins!")
while roll != 5:
    name = input('Enter a name, or \'q\' to quit:  ' )
    if name == 'q':
        print('You left the game')
        break;
    count += 1
    roll = random.randint(1,5)
    print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')
print(f'You roll the dice {count} times')

# Third problem: same problem but when we use a 'enter' as name of the person, the program 'continues'
# 'continue' instruction does that the program skip all the code bellow the instruction and start the iteration again

roll = 0
count = 0
print("First person to roll a '5' wins!")
while roll != 5:
    name = input('Enter a name, or \'q\' to quit:  ' )
    if name.strip() == '': #with strip function we can skip all the spaces in the edges of our input word
        continue
    if name.strip() == 'q':
        print('You left the game')
        break;
    count += 1
    roll = random.randint(1,5)
    print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')
print(f'You roll the dice {count} times')
