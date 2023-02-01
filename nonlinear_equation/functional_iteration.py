# 非線形方程式の解法
# Contents
# 関数反復法(浮動点反復法)
def g(x):
    #f(x)=0から同値変形でx=g(x)にする
    # return
    pass

def functional_iterarion(x, tol): #tol: 許容誤差 #TODO: deltaの計算方法考えないと。2乗ノルムとか
    x=0
    delta=0
    while delta>tol:
        y=g(x)
        delta=y-x
        x=y
    return x
