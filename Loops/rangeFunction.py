# simple range function
a = range(10)
print(a)
print('\n')

for i in a:
    print(i)
print('\n')

# Range with only one argument, STOP - starts from 0 till the stop value
for i in range(5):
    print(i)
print('\n')

# Range with 2 arguments, START and STOP - inclusive of START and exculusive of STOP
for i in range(10,20):
    print(i)
print('\n')

# Range with 3 argumanets, START, STOP and INTERVAL - inclusive of START and exculusive of STOP with INTERVAL steps
for i in range(0,20,2):
    print(i)
print('\n')

