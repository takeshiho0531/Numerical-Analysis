# 定常反復法

#行列XとYの積を計算
def matmul(X,Y): 
    for i in range(len(X)):
        matmul = [[0]*len(X)]*len(Y[0])
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                matmul[i][j]=X[i][k]*Y[k][j]
    return matmul

# 上三角(-対角成分),対角成分、下三角(-対角成分)に行列を分ける関数
def split_into_DLU(A):
    D=A.copy()
    L=A.copy()
    U=A.copy()
    for i in range(len(A)):
        for j in range(len(A)):
            if i>j:
                D[i][j]=0
                U[i][j]=0
            elif i==j:
                U[i][j]=0
                L[i][j]=0
            else:
                D[i][j]=0
                L[i][j]=0

    return D,L,U


# Jacob法
def Jacobian_iteration(A, b,x0): # Aは係数行列、bは拡大係数行列から係数行列除いた部分の行列
    D,L,U=split_into_DLU(A)
    Dinv=D.copy()
    for i in range(len(D)):
        Dinv[i][i]=1/D[i][i]

    x=x0
    delta=x0
    while delta > 1e-6:
        delta= -1*matmul(matmul(Dinv, L+U), x)+matmul(Dinv, b) - x
        x = -1*matmul(matmul(Dinv, L+U), x)+matmul(Dinv, b)
    return x


# Gauss-Seidel
def Gauss_Seidel(A):
    D,L,U=split_into_DLU(A)
    DLinv=D.copy()
    for i in range(len((DLinv))):
        for j in range(len(len(DLinv))):
            #いや、上三角やからって普通に逆行列求めるのむずくない？？普通に分解しそうな勢いなんだが。



    

