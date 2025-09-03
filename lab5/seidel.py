import math
import matplotlib.pyplot as plt
temp_x=[]
temp_y=[]
def jacobi_method(a1,b1,c1,a2,b2,c2):
    x=0
    y=0
    iterations=1000
    for i in range(0,iterations):
        old_x=x
        old_y=y
        x=(c1-b1*old_y)/a1
        y=((c2-a2*x)/b2)
        error_x=abs(old_x-x)
        error_y=abs(old_y-y)
        temp_x.append(old_x)
        temp_y.append(old_y) 
        if error_x<tolerence and error_y<tolerence:
            print(f"answer for x:{x},y:{y} after iteration {i}")
            return x,y
    print("max iterations reached")
    print(f"x:{x},y:{y}")
    return x,y
a1,b1,c1,a2,b2,c2=3,1,8,5,5,20
tolerence=0.001
jacobi_method(a1,b1,c1,a2,b2,c2)

plt.plot(temp_x,temp_y)
plt.xlabel("x -->")
plt.ylabel("y -->")
plt.show()


plt.plot(temp_x,label="x")
plt.plot(temp_y,label="y")
plt.legend()
plt.xlabel("iterations -->")
plt.ylabel("predicted values -->")
plt.show()