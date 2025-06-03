# name = input('What is your name:')

# print('Hello!',name,' welcome to python')
# a,b = input('\nGive us 2 mubers:').split()

# print('\nThese are the 2 numbers you have given: ',a,b)

# operator = 0
# while(operator == 0):
#     operator = input('\nTell us what operation do we have to do with this number:')
#     a=int(a)
#     b=int(b)
#     if operator == '+':
#         print('Sum is: ',a+b)
#     elif operator == '-':
#         print('Difference is:',a-b)
#     elif operator == '*' or operator == 'x':
#         print('Product is:', a*b)
#     elif operator == '/':
#         print('Division is:',a/b)
#     else:
#         print('Invalide operator, you must choose any one of +,-,*,/ only')
#         operator = 0

# print('Good bye!')

# Multiple inputs and type convertion

[a, b, c] = [int(x) for x in input('Enter 3 numbers: ').split()]
print(f'Numbers are {a}, {b} and {c}')
