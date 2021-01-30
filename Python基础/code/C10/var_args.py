#可变参数---函数的参数个数可变
#可变参数---参数个数可变的又一种方法
def multi_sum( x, *args ):
    #列表或者元组作为函数的参数的时候，定义的时候，要用*进行解构
    s = x * sum( args )
    return s
print('元组做函数参数:', multi_sum(2, 3, 4, 5) ) #把3，4，5封装元组了
#字段作为函数的参数**dargs
def mul_sum_sumdict( x, *args,**dargs):
    #列表或者元组作为函数的参数的时候，定义的时候，要用*进行解构
    #字典做函数的参数时，得用**,实现函数参数个数可变
    s = x * sum( args )
    for v in dargs.values():
        s += v
    return s

#字典参数的调用: a=6
print( mul_sum_sumdict(2, 3, 4, 5,a=6) )  
#字典参数的调用: a=6,b=10
print( mul_sum_sumdict(2, 3, 4, 5,a=6,b=10) )  
