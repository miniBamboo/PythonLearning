#函数参数和返回值
'''
def sum2num():
    x,y = 2,5
    z = x+y
    print("{}+{}={}".format(x,y,x+y))
sum2num()
'''
'''
def sum2num(x,y):
    #x,y = 2,5
    z = x+y
    print("{}+{}={}".format(x,y,x+y))
sum2num(3,6)
sum2num(13,12)
'''
#实现数学函数的嵌套调用
def sum2num(x,y):
    #x,y = 2,5
    z = x+y
    #print("{}+{}={}".format(x,y,x+y))
    return z
def mul2num(a,b):
    #z = x*y
    return a*b
print(2*sum2num(5,7))
print(sum2num(12,56)/2)
#2*(3+5)
print(mul2num(2,sum2num(3,5))) #函数的实参(调用参数)为函数
def div2num(x,y):
    return x/y
print(div2num(sum2num(12,56),2))
