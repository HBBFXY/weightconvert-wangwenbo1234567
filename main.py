W = input('请输入需转换的重量；')
if W[-1] in ['g']:
    D = eval(W[0:-2])*22.046
    P = int(D*1000)
    p = float(P/1000)
    print('转换后的重量为%.3f pd'%p)
elif W[-1] in ['d']:
    G = eval(W[0:-2])/22.046
    K = int(G*1000)
    k = float(K/1000)
    print('转换后的重量为%.3f kg'%k)
else:
    print('输入格式错误')
