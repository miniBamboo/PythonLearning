#变量作用域
'''
n = 100
def func(x,y):    
    n = x+y
    return n
print(func(2,3),n)


def func2(x,y):
    n =10
    z = x+y+n
    return z
print(func2(2,3),n) #调用func2


def func3(x,y):
    global n
    n = x+y
    return n
print(func3(2,3),n) #调用func3

n = 200
def func4(x,y):
    z = x+y+n
    return z
print(func4(2,3),n) #调用func4

def func5(x,y): #建议用 
    global n
    z = x+y+n
    return z
print(func5(2,3),n) #调用func5
'''
#函数中定义全局变量(尽量不要这么做 ):
def ff(x,y):
    global m
    m = x+y
    return m
def ff2(x,y):
    global m
    z = x+y+m
    return z
ff(2,3)
print(ff2(4,5))

