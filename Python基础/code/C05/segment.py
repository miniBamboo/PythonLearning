#分段函数:
x=float(input('x:'))
if x>= 1:
    y= 2*x+1
elif x>=0: # 1>x>=0  # x<1 and x >= 0
    y = x**2
elif x>=-1:
    y = 1-x*x
else:
    y = -x
print('y = ',y)
