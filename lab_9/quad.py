import math
node_table = {
    1: {
        "nodes": [0.0],
        "weights": [2.0]
    },
    2: {
        "nodes": [-0.5773502691896257, 0.5773502691896257],
        "weights": [1.0, 1.0]
    },
    3: {
        "nodes": [-0.7745966692414834, 0.0, 0.7745966692414834],
        "weights": [0.5555555555555556, 0.8888888888888888, 0.5555555555555556]
    },
    4: {
        "nodes": [-0.8611363115940526, -0.3399810435848563,
                   0.3399810435848563, 0.8611363115940526],
        "weights": [0.34785484513745385, 0.6521451548625461,
                    0.6521451548625461, 0.34785484513745385]
    },
    5: {
        "nodes": [-0.9061798459386640, -0.5384693101056831, 0.0,
                   0.5384693101056831, 0.9061798459386640],
        "weights": [0.2369268850561891, 0.4786286704993665,
                    0.5688888888888889, 0.4786286704993665,
                    0.2369268850561891]
    }
}

def f(x):
    return math.sin(math.pi/4*(x+1))
for i in node_table.keys():
    ans=0
    for j in range(i):
        ans+=f(node_table[i]["nodes"][j])*node_table[i]["weights"][j]
    print(f"value for number of nodes {i} is {ans} and the value of 4/pie is {4/math.pi}")
    print(f"this node has a relative error with 4/pie as {abs(ans-4/math.pi)/math.pi*100}")