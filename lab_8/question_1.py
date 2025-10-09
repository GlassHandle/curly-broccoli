def forward(x,f,h=0.25):
    return (f(x+h)-f(x))/h
def backward(x,f,h=0.25):
    return (f(x)-f(x-h))/h
def central(x,f,h=0.25):
    return (f(x+h)-f(x-h))/(2*h)
def f(x):
    return -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2
def f_der(x,f,h=0.25):
    return (f(x+h)+f(x-h)-2*f(x))/(h**2)
def deri(x):
    return -0.4 * x**3 - 0.45 * x**2 - x - 0.25
def sec(x):
     return -1.2 * x**2 - 0.9 * x - 1
a=forward(0.5,f)
b=deri(0.5)
print(f"value using forward differnce is {a} with relative error {abs((a-b)/b)*100}")
a=backward(0.5,f)

print(f"value using backward differnce is {a} with relative error {abs((a-b)/b)*100}")
a=central(0.5,f)

print(f"value using central differnce is {a} with relative error {abs((a-b)/b)*100}")

print(f"value of second derivative is {f_der(0.5,f)}")
print(f"second diffivative exact value is {deri(0.5)}")
print("------------second deivative--------------------")
a=forward(0.5,deri)
b=sec(0.5)
print(f"value using forward differnce is {a} with relative error {abs((a-b)/b)*100}")
a=backward(0.5,deri)

print(f"value using backward differnce is {a} with relative error {abs((a-b)/b)*100}")
a=central(0.5,deri)

print(f"value using central differnce is {a} with relative error {abs((a-b)/b)*100}")

print(f"value of second derivative is {f_der(0.5,f)}")
print(f"second diffivative exact value is {sec(0.5)}")