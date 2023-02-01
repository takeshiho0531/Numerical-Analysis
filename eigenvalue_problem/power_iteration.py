# 固有値問題の解法
# Contents
# 冪乗法
# 逆反復
# シフト付き逆反復

from simultaneous_linear_equations.LU_decomposition import LU_decomposition
#行列XとYの積を計算
def matmul(X,Y): 
    for i in range(len(X)):
        matmul = [[0]*len(X)]*len(Y[0])
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                matmul[i][j]=X[i][k]*Y[k][j]
    return matmul


# 冪乗法
# 絶対値最大の固有値が求まる
def power_iteration(A,x0,m): #TODO: これmって自分で決めないといけないの？？
    x=x0
    for i in range(m):
        y=matmul(A,x)
        x=y/matmul(y,y.T)
    return x 

# 逆反復
# 絶対値最小の固有値が求まる
def inverse_iteration(A,x0,m):
    L,U=LU_decomposition(A)
    x=x0
    for i in range(m):
        B=x.copy()
        for k in range(len(x)):
            sum=0
            for l in range(k-1):
                sum+=L[k][l]*B[l]
            B[k]=(x[k]-sum)/L[k][k]
        
        y=B.copy()
        for k in range(len(x)):
            sum=0
            for l in range(k-1):
                sum+=U[len(y)-k][len(y)-l]*y[len(y)-l]
            y[len(y)-k]=(B[len(y)-k]-sum)/U[len(y)-k][len(y)-k]
        x=y/matmul(y,y.T)
    return x


# シフト付き逆反復
# muに固有値が最近接の固有ベクトルを求める
def inverse_iteration_with_shift(A,x0,m,mu):
    for i in range(len(A)):
        A[i][i]-=mu
    x=inverse_iteration(A,x0,m)
    return x



