# 直接法　LU分解

# 枢軸選択なしLU分解
def LU_decomposition_with_no_pivot_selection(A): # Aは係数行列!! 拡大係数行列ではないよ。
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            A[j][i]=A[j][i]/A[i][i]
            for k in range(i+1, len(A)):
                A[j][k]=A[j][k]-A[i][k]*A[j][i]
    # 後分解するだけ
    L=A.copy()
    U=A.copy()
    for i in range(len(A)):
        L[i][i]=1
        for j in range(len(A)):
            if i<j:
                L[i][j]=0
            elif i>j:
                U[i][j]=0
    return L,U

# 枢軸選択ありLU分解
def LU_decomposition(A):
    for i in range(len(A)):
        pivot= max(A[:,i])
        pivot_row=A[:,i].index(pivot)[0] #TODO
        former_pivot=A[i+1].copy()
        A[i+1]=A[pivot_row]
        A[pivot_row]=former_pivot

        for j in range(i+1, len(A)):
            A[j][i]=A[j][i]/A[i][i]
            for k in range(i+1, len(A)):
                A[j][k]=A[j][k]-A[i][k]*A[j][i]

    # 後分解するだけ
    L=A.copy()
    U=A.copy()
    for i in range(len(A)):
        L[i][i]=1
        for j in range(len(A)):
            if i<j:
                L[i][j]=0
            elif i>j:
                U[i][j]=0
    return L,U
    


