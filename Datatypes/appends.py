# simple append
a = [10, 'hello']
a.append(10.20)
print(a)

# appending a list to list, here the whole list will be set to the index, like nested list
a.append([1000, 2000])
print(a)

# difference between append and extend
a.extend([3000,4000])
print(a)