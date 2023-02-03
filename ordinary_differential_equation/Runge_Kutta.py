# 常微分方程式の解法
# Contents
# 4次Runge-Kutta法

def f(x,t): 
    # 計算したい式を入れる
    # return 
    pass

def Runge_Kutta(y0,m,t):
    y=y0
    Y=[]
    Y.append(y)
    for i in range(m):
        k1=f(y,m*t)
        k2=f(y+1/2*k1*t, (m+1/2)*t)
        k3=f(y+1/2*k2*t, (m+1/2)*t)
        k4=f(y+k3*t, (m+1)*t)
        y=y+t*(1/6*k1+1/3*k2+1/3*k3+1/6*k4)
        Y.append(y)
    return Y
