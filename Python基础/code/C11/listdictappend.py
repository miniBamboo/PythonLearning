#完全重写的方法：
#读
f = open("listdict.txt","rt")   #t表示文本文件方式
listdict = eval(f.read())
f.close()
print(listdict)

#添加
dictscore={'id': 18041100, 'name': '赵六', 'Python': 75, '材料力学': 77}
listdict.append(dictscore)
print(listdict)
print()
#删除
del listdict[1] #1为列表下标
#listdict.remove(dictscore)
#重写
f = open("listdict.txt","wt")
f.write(str(listdict))
f.close()

