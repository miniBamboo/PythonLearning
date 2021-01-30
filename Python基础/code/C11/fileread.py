f = open("a.txt","rt")   #t表示文本文件方式
#f = open("a.txt","rb")
#print(f.readline())
#print(f.readlines())
print(type(f))
print(f.read())
f.close()
