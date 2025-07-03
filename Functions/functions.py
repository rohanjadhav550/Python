# simple function
def fun():
    print('This is a function')

fun()

# function with argument
def fun1(a):
    print(a)

fun1(10)

# default argument
def fun2(a, b=10):
    print(a , b)

fun2(20)

# Named arguments
def fun3(name1, name2):
    print(name1, name2)

fun3(name2=10, name1=20)

# Recursive function
def recFun(num, pointer):
    if num == pointer:
        print('Found')
    elif num < pointer:
        print(num)
        recFun(num+1, pointer)
    else:
        print(num)
        recFun(num-1,pointer)

recFun(1,10)

# inner function
def outFun(num):
    def innerFun():
        print(num)
    innerFun()

outFun(10)