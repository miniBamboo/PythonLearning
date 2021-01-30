#递推公式类型的编程题(有正负号)
# s = 1/1-1/3+1/5-...+1/101
'''
s=0
sign = -1 # 1
for n in range(0,51): # 
    sign = -sign
    s = s + sign/(2*n+1) # s += sign/(2*n+1) 
print("s=%f"%s)
'''
s=0
sign = -1 # 1
for n in range(1,102,2):
    sign = -sign
    s = s + sign/n # s += sign/(2*n+1)
print("s=%f"%s)

