# Normal loop example
loopValues = ['Hello', 10, 20.45, True, 'World!']

for i in loopValues:
    print(i)
print()
# Looping through string, the string will act as array of chars
a = 'Sample String'
for i in a:
    print(i)
print()

# For loop with range
for i in range(0,5,2):
    print(i)
print()

# use of continue keyword in for loop
for i in range(0,20):
    if i%2 != 0:
        continue
    print(i)
print()

# use of break keyword
for i in range(2,20):
    if i % 2 != 0:
        break
    print(i)
print()