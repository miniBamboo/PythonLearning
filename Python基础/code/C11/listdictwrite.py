listdict=[{'id':18041100,'name':'张三','Python':99,"材料力学":71},
          {'id':18041181,'name':'李四','Python':34,'材料力学':98},
          {'id':18041182,'name':'王五','Python':60,'材料力学':72}]
f = open("listdict.txt","wt")   #t表示文本文件方式
f.write(str(listdict))

f.close()
