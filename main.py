W = input('请输入需转换的重量；')
if W[-1] in ['g']:
    D = eval(W[0:-2])*22.046
    print('转换后的重量为%.3f pd'%D)
elif W[-1] in ['d']:
    G = eval(W[0:-2])/22.046
    K = int(G*1000)
    k = float(K/1000)
    print('转换后的重量为%.3f kg'%k)
else:
    print('请输入正确的单位')
