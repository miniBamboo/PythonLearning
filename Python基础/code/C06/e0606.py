#for else的使用(while else的使用)
n=int(input('判断是否素数，先输入一个整数:'))
for i in range(2,n-1):
    if n%i==0: #整除
        print(n,"不是素数")
        break
else:
    print(n,"是素数")
 
