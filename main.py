W = input('请输入需转换的重量；')
if W[-1] in ['g']:
    D = eval(W[0:-2])*2.2046
    print('转换后的重量为%.3f'%D)
elif W[-1] in ['d']:
    G = eval(W[0:-2])/2.2046
    print('转换后的重量为%.3f'%G)
else:
    print('请输入正确的单位')
