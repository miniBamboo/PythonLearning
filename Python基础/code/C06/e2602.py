#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={:<2d}\t'.format(i,j,i*j),end=' ')
    print('')
