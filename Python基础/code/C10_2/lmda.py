#lamda表达式

'''
func = lambda x,y:x+y
print(func(2,3))
print(type(func))
#lambda x,y:x+y功能：
#def xxx(x,y):
#   return x+y

def calcu(x,y,callfunc):
    return callfunc(x,y) #
print(calcu(2,3,lambda a,b:a**b)) #return (lambda x,y:x*y)
'''
num = [1,2,3,4,5]
#def s2(x):
#   return x*x
num2 = map(lambda x:x*x*x,num)
print(list(num2))
print(num2)

