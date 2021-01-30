#递推公式类型的编程题
'''# s = 0+2+4+...+100
s=0
n=0
while n<=50:
    s = s + n+n # s += n
    n += 1 # n = n + 1
print("s=%d"%s)
'''
'''s=0
n=0
while n<=100:
    s = s + n # s += n
    n += 2 # n = n + 1
print("s=%d"%s)
'''
'''s=0
for n in range(51): # 
    s += 2*n
print("s=%d"%s)
'''
s=0
for n in range(0,101,2): # 奇数和：range(1,100,2)
    s += n
print("s=%d"%s)
