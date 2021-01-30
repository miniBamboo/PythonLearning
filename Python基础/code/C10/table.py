def table99():
    '''
    99乘法表打印
    '''
    for i in range(1,10):
        for j in range(1,i+1):
            print("%1d*%1d=%2d"%(i,j,i*j),end=" ")
        print("")
#table99()
