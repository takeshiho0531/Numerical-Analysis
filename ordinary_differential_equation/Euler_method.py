# 常微分方程式の解法
# Contents
# 陽的オイラー法
# 陰的オイラー法

from nonlinear_equation import Newton_Raphson_method

def f(x,t): 
    # 計算したい式を入れる
    # return 
    pass

# explicit_method
def explicit_mothod(m,y0,t): #t: 時間幅
    Y=[]
    y=y0
    Y.append(y)
    for i in range(m):
        y=y+f(y,i*t)
        Y.append(y)
    return Y

# implicit_mothod
def implicit_method(m,y0,t,tol):
    Y=[]
    y=y0
    Y.append(y)
    for i in range(m):
        y=Newton_Raphson_method(y,tol)
        Y.append(y)
    return Y

