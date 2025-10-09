import numpy as np
import math
def f(x1,x2,x3):
    return np.array([
        3*x1 - 0.5 - np.cos(x2 * x3),
        -81 * (x2 + 0.1)**2 + x1**2 + np.sin(x3) + 1.06,
        20 * x3 - (3 - 10*np.pi)/3 + np.exp(-x1 * x2)
    ])
def jacobian(x1,x2,x3):
    s = np.sin(x2 * x3)
    return np.array([
        [3,           x3 * s,                x2 * s],
        [2 * x1,      -162 * (x2 + 0.1),      np.cos(x3)],
        [-x2 * np.exp(-x1 * x2),  -x1 * np.exp(-x1 * x2),  20]
    ])
def newton_raphson(x1,x2,x3):
    X=np.array([x1,x2,x3])
    iterations=100000
    for i in range(iterations):
        x1,x2,x3=X
        X=X-np.linalg.inv(jacobian(x1,x2,x3))@f(x1,x2,x3)
        if abs(np.linalg.norm(f(x1,x2,x3),ord=np.inf))<0.0001:
            print(f"answer for the equation is {X}")
            return
    print(f"max iterations reached answer is {X}")
newton_raphson(0.1,0.1,-0.1)