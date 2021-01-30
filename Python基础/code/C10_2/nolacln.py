def calnum(x,y,z):
    n = 0
    def mul2num(x,y):
        return x*y
    n= z+mul2num(x,y)
    return n
print(calnum(2,3,4))
#内部函数，没有被调用和调用了的效果
def calnum2(x,y,z):
    n = 0
    def mul2num(x,y):
        return n+ x*y
    #n= z+mul2num(x,y)
    #return n
print(calnum2(2,3,4)) #没有被调用,结果是None
#
def calnum3(x,y,z):
    n = 0
    def mul2num(x,y):
        return n+ x*y
    #n= z+mul2num(x,y)
    return n
print(calnum3(2,3,4))

def calnum4(x,y,z):
    n = 1
    def mul2num(x,y):
        nonlocal n
        return n+ x*y
    n= z+mul2num(x,y)
    return n
print(calnum4(2,3,4))
