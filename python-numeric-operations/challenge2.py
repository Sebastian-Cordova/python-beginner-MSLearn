# Build a simply calculator
print("Welcome to Sebas's Calculator")

#Verification
value1 = input('Please input a number ')
if value1.isnumeric() == False:
    print('Wrong input, you should enter a number.')
    exit()
operation = input('Enter the operation: ')
if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '//' and operation != '**':
    print('Operation not recognized')
    exit()
value2 = input('Second number? ')
if value2.isnumeric() == False:
    print('Wrong input, you should enter a number.')
    exit()
#Operate
value1 = int(value1)
value2 = int(value2)
if operation == '+':
    result = value1 + value2
elif operation == '-':
    result = value1 - value2
elif operation == '*':
    result = value1 * value2
elif operation == '/':
    result = value1 / value2
elif operation == '//':
    result = value1 // value2
elif operation == '**':
    result = value1 ** value2

print(f'The result of {value1} {operation} {value2} = {result}')
