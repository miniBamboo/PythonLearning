num = [1,3,5,7,9,2,4,6,8,10,20,0,31]
#推导式
print("推导式")
num_sqr=[v*v for v in num]
print(num_sqr)
num_less10 = [v for v in num if v<10]
print(num_less10)
#生成器:
print("生成器:")
iters=(v for v in num)
print(iters)
print(next(iters))
print(next(iters))
print(tuple(iters))
#iter()生成器
iterss = iter(num)
print(iterss)
print(next(iterss))
print(next(iterss))
print(list(iterss))
