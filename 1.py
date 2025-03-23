import numpy as np


def cal(n, h):  # 回弹次数以及初始高度
    x = h  # 回弹高度
    g = 9.8
    t = np.sqrt(2 * h / g)
    T = 0  # 总时间
    s = 0  # 总路程
    for i in range(0, n):
        # 下落
        T += t
        s += x
        x = x / 2  # 更新高度
        t = np.sqrt(2 * x / g)  # 更新时间
        # 回弹
        T += t
        s += x
    return T, s, x


h = 100
T, s, x = cal(10, 100)
print(T, s, x)