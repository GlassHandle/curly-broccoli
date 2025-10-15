import math
def f(x):
    return math.sin(x)
def integrate_simpsons(a,b,n=11):
    h=(b-a)/(n-1)
    k=0
    ans=0
    x=a
    while a+k*h<=b:
        x=a+k*h
        if x==a or x==b:
            ans+=f(x)
        elif k%2==0:
            ans+=2*f(x)
        else:
            ans+=4*f(x)
        k+=1
    return h/3*ans
def trapezoidal(a,b,n=11):
    h=(b-a)/(n-1)
    mul=h
    ans=f(a)+f(b)
    while a+h<b:
        ans+=2*f(a+h)
        a+=h
    return ans*mul/2
n=11
print("answer using the simphsons:",integrate_simpsons(0,math.pi/2,n))

print("answers using the trapazoidal",trapezoidal(0,math.pi/2,n))
