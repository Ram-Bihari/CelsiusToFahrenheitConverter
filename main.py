import time

print('Welcome to Celsius to Fahrenheit converter!')
choice = int(input('Enter 1 to convert Fahrenheit to Celsius, and 2 for Celsius to Fahrenheit'))
value = int(input('Cool! Enter the temprature!'))

if choice == 1:
    sub = value - 32
    temp = sub * 5/9
    print('Your answer is ',temp, 'Celsius')
elif choice == 2:
    sub = value * 9/5
    temp = sub + 32
    print('Your answer is ',temp, 'Fahrenheit')

time.sleep(2)
print('Thanks for using this converter! See you soon!')
