def f(x):
    return x**3-5*x+1
def df(x):
    return 3*x**2-5

a = int(input("Enter the start of range: ", ))
b = int(input("Enter the end of the range: "))
intervals = []
for i in range(a,b):
    if(f(i)*f(i+1)<0):
        intervals.append((i,i+1))
print("List of intervals in range given: ",intervals)
for interval in intervals:
    u,v = interval
    r0 = (u+v)/2
    print("For interval: ",interval)
    n = int(input("Enter number of iterations: ", ))
    for i in range(n):
        r1 =r0-(f(r0)/df(r0))
        err = abs(r1-u)
        r0 = r1
        print(f'For iteration {i+1} root is {r1} and error is {err}')