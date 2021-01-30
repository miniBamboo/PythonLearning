#递推公式类型的编程题
'''
#s=0+1+2+..+100
s=0
n=0
while n<=100:
    s = s + n # s += n
    n += 1 # n = n + 1
print("s=%d"%s)
'''
s=0
for n in range(101): # 
    s += n
print("s=%d"%s)

