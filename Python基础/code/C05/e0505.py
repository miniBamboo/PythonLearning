#三元表达式与if语句的对比
a=3
b=4
'''
if a>b:
    x=a
else:
    x=b
print("max:",x)
'''

#x= a if a>b else b
#print("max:",x)

print("max:",a if a>b else b)
