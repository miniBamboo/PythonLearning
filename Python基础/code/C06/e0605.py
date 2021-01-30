#break和coninue的使用
'''i = 0
while i < 10:
    #break #某一条件满足时，退出循环，不再执行后续重复的代码
    #i = 3
    if i == 3: #or i==4:
        #print('continue:',i)
        #break
        i += 1
        continue
    print(i)
    i += 1
print("over")
'''
for i in range(10):    
    #break #某一条件满足时，退出循环，不再执行后续重复的代码
    #i = 3
    if i == 3: #or i==4:
        #print('continue:',i)
        #break
        continue
    print(i)
print("over")
