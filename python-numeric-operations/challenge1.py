# Write a program to convert temperatures from Fahrenheit to Celsius

fahren_grades = input('What is the temperature in fahrenheit?')
if fahren_grades.isnumeric() == True: #This method can only be applied when the variable stills being a string
    celsius = (int(fahren_grades) - 32) * 5/9
    print(f'Temperature in celsius is: {int(celsius)}')
    exit() #We can use this instruccion, also we can skip this if we dont want to stop the logic.
else:
    print('Input is not a number')