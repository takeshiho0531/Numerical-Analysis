# 直接法：ガウスの消去法

# 枢軸選択なしガウスの消去法
def gaussian_elimination_with_no_pivot_selection(A): #A:拡大係数行列
    for i in range(len(A)):
        for j in range(len(A)-1):
            m=A[j][i]/A[i][i]
            for k in range(len(A[0])):
                A[j][k] = A[j][k]-m*A[i][k]
    B=A[:,-1]
    X=B.copy()
    for l in range(len(A)):
        AX = 0
        for m in range(l-1):
            AX += A[len(A)-l][len(A)-m]*X[len(A)-m]
        X[len(A)-l]=(B[len(A)-l]-AX)/A[len(A)-l][len(A)-l]
    return X

# 枢軸選択付きガウスの消去法
def gaussian_elimination(A): #A:拡大係数行列
    for i in range(len(A)):
        for j in range(i+1, len(A)-1):
            pivot=max(A[:,i])
            pivot_row=pivot.index(A)[0] #TODO
            A_pivot = A[pivot_row] #TODO
            A[i+1]=A_pivot #TODO
            A[pivot_row]=A[i+1] #TODO

            m=A[j][i]/A[i][i]
            for k in range(len(A[0])):
                A[j][k] = A[j][k]-m*A[i][k]
    B=A[:,-1]
    X=B.copy()
    for l in range(len(A)):
        AX = 0
        for m in range(l-1):
            AX += A[len(A)-l][len(A)-m]*X[len(A)-m]
        X[len(A)-l]=(B[len(A)-l]-AX)/A[len(A)-l][len(A)-l]
    return X

