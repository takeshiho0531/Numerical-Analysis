# 非線形方程式の解法
# Contents
# Newton-Raphson法

from simultaneous_linear_equations.LU_decomposition import LU_decomposition
def f(x):
    # return 求めたい非線形方程式
    pass

def Jacobian_matrix(x):
    #return (自分で解析的に手計算)
    pass

def Newton_Raphson(x0, tol):
    x=x0
    delta=0
    while delta>tol:
        L,U=LU_decomposition(Jacobian_matrix(x))
        B=f(x).copy()
        for i in range(len(B)):
            sum=0
            for j in range(i):
                sum+=L[i][j]*B[j]
            B[i]=(f(x)[i]-sum)/L[i][i]
        y=B.copy()
        for i in range(len(y)):
            sum=0
            for j in range(len(y)-i):
                sum+=L[len(y)-i][j]*B[j]
            y[len(y)-i]=(B[len(y)-i]-sum)/U[len(y)-i][len(y)-i]
        delta=y
        x=x+y
    return x




