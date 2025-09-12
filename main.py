#weightConvert
W = input('请输入需转换的重量；')
if W[-1] in ['G','g']:
    W = eval(W[0:-2])*2.2046
    print('转换后的重量为%.3f'%W)
elif W[-1] in ['D','d']:
    W = eval(W[0:-2])/2.2046
    print('转换后的重量为%.3f'%W)
else:
    print('请输入正确的单位')
