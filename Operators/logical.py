a,b = map(bool, input('Enter 2 booleans:').split())

# AND operation
if a and b:
    print(f'{a} AND {b} is TRUE')

# OR operation
if a or b:
    print(f'{a} OR {b} is TRUE')

# NOT operation
if not a:
    print(a)