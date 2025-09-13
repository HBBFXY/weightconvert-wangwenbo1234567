#weightConvert
W = input('请输入需转换的重量；')
if W[-1] in ['G','g']:
    D = eval(W[0:-2])*2.2046
    print('转换后的重量为%.3f pd'%D)
elif W[-1] in ['D','d']:
    G = eval(W[0:-2])/2.2046-0.001
    print('转换后的重量为%.3f kg'%G)
else:
    print('请输入正确的单位')
