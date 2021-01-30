f = open("listdict.txt","rt")   #t表示文本文件方式
listdict = eval(f.read())
f.close()
print(listdict)
print(type(listdict))
