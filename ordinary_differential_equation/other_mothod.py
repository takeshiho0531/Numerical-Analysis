# 常微分方程式の解法
# Contents
# 中点則
# 台形則
# 陰的中点則

from nonlinear_equation import Newton_Raphson_method

def f(x,t): 
    # 計算したい式を入れる
    # return 
    pass

def F1(x,t):
    # 台形則で解くべき非線形方程式書く
    pass

def F2(x,t):
    # 陰的中点則で解くべき方程式を書く
    pass

# 中点則
def midpoint_rule(y0,y1,t,m): # t: 時間幅 m: ステップ数
    y_1=y0
    y_2=y1
    Y=[]
    Y.append(y_1)
    Y.append(y_2)
    for i in range(m):
        y=2*t*f(y_1,m*t)+y_2
        Y.append(y)
        y_1=y_2
        y_2=y
    return Y


# 台形則
def trapezoidal_rule(y0,t,m):
    y=y0
    Y=[]
    Y.append(y0)
    for i in range(m):
        y=Newton_Raphson_method(F1(y,t))
        Y.append(y)
    return Y

# 陰的中点則
def implicit_midpoint_rule(y0,t,m):
    y=y0
    Y=[]
    Y.append(y0)
    for i in range(m):
        y=Newton_Raphson_method(y,t)
        Y.append(y)
    return Y
    



        






