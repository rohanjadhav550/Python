gl = 'This is a global variable'
print(gl)
def innerFun():
    gl = 'This is local variable'
    print('Local variable:',gl)

def innerFun1():
    global gl
    print(gl)

innerFun()
innerFun1()