flag = True

while flag:
    answer = input('Would you like to continue?')
    if answer == 'yes' or answer == 'Yes':
        print('Continuing ...')
        print('Complete!')
        flag = False
    elif answer == 'no' or answer == 'No':
        print('Exiting')
        flag = False
    else:
        print('Please try again and respond with yes or no.')