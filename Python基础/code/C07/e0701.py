#异常处理
#n = eval(input("请输入一个数字: "))
#print("输入数字的3次方值为: ", n**3)
try:
    n = eval(input("请输入一个数字: "))
    print("输入数字的3次方值为: ", n**3)
except:
    print("输入错误，请输入一个数字!")
else:
    print('ok')
finally:
    print('输入了一次')
    
# 强制输入一个数字
'''while True:
    try:
        n = eval(input("请输入一个数字: "))
        break
    except:
        print("输入错误，请输入一个数字!")
        continue
print("输入数字的3次方值为: ", n**3)
'''
