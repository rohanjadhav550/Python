# Formatting string using format() method

# name, age, gender = input('Please enter your name, age, gender respectivly: ').split()

# print('Hello {0}, good to have a friend of {1} years!'.format(name, age))

# possitioned and named parameter
print('Best place in the world is {0}, and best work is {work}'.format('Home', work='farming'))

# interger and float value formatting.
print('This is integrer value: {0:2d}, This is float vallue: {1:8.2f}'.format(10,230004.2345))

# String function to format the content
# center aligned
print(' Center aligned: '.center(40,'#'))

# left aligned
print('Content text '.ljust(40,'-'))

# Right aligned
print(' Content'.rjust(40,'*'))

amount = 1000.267
print('The amount is: {:.2f}'.format(amount))

# sep usage
print('Hello', 'Rohan', 'How', 'are', 'you', 10, 20.3, sep='-')

# end
print('Hello there', end='@')

#f-string
first_name = 'Rohan'
last_name = 'Jadhav'

print(f'\n{first_name}. {last_name}, is a backend developer from India')

# Date models 
from datetime import date, time, datetime
date1 = date.today()
print(f'Today\'s date is: {date1}')

# normal usage
date2 = date(2025, 12, 5)
print(f'Date: {date2}')

# getting day, month and year
date3 = date.today()
print(f'Day: {date3.day}')
print(f'Month: {date3.month}')
print(f'Year: {date3.year}')

# Time
# normal usage
time1 = time(13, 12, 34)
print(f'Time: {time1}')

# Hr., Min., Sec.

print(f'Time: {time1}')
print(f'Hr. : {time1.hour}')
print(f'Min.: {time1.minute}')
print(f'Sec.: {time1.second}')

#datetime
# normal
datetime1 = datetime(2025, 6, 2, 12, 12, 12)
print(f'Date-Time: {datetime1}')

# current date and time
datetime2 = datetime.now()
print(f'Current date-time: {datetime2}')

# extracting each part of date time
datetime3 = datetime.now()
print(f'Day: {datetime3.day}')
print(f'Month: {datetime3.month}')
print(f'Year: {datetime3.year}')
print(f'Year: {datetime3.hour}')
print(f'Year: {datetime3.min}')
print(f'Year: {datetime3.second}')
print(f'Year: {datetime3.microsecond}')