from functools import lru_cache
@lru_cache
def f(arr):
    if len(arr)==1:
        return l(arr[0])
    else:
        return (f(arr[1:])-f(arr[:-1]))/(arr[-1]-arr[0])
def answer(x,points):
    ans=0
    for i in range(len(points)):
        term=f(points[:i+1])
        for j in points[:i]:
            term*=(x-j)
        ans+=term
    return ans
points=[1,4,6,5]
def l(x):
    if x==1:
        return 0
    if x==4:
        return 1.386294
    if x==6:
        return 1.791759
    if x==5:
        return 1.609438
a=answer(2,points)
print(f"value of the function at 2 is {a} with relative error {abs((a-0.6931472)/0.6931472)*100}%")