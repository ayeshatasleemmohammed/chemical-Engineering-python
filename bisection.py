import math
def f(x):
    return x**3-5*x+1
a = int(input("Enter the start of range: ", ))
b = int(input("Enter the end of the range: "))
intervals = []
for i in range(a,b):
    if(f(i)*f(i+1)<0):
        intervals.append((i,i+1))
print("List of intervals in range given: ",intervals)
for interval in intervals:
    u,v = interval
    print("For interval: ",interval)
    z = int(input("Enter the number of significant digits: ", ))
    e = 10**(-z)
    n = (math.log(v-u)-math.log(e))/math.log(2)
    n = math.ceil(n)
    for i in range(n):
        r = (u+v)/2
        err = abs(r-u)
        if(f(u)*f(r)<0):
            v = r
        elif(f(v)*f(r)<0):
            u = r
        print(f'For iteration {i+1} root is {r} and error is {err}')
