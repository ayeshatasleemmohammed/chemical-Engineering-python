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
    r0,r1 = interval
    print("For interval: ",interval)
    n = int(input("Enter number of iterations: ", ))
    for i in range(n):
        r = (r0*(f(r1))-r1*(f(r0)))/(f(r1)-f(r0))
        err = (r-r0)
        if(f(r)*f(r0)<0):
            r1 = r
        elif(f(r)*f(r1)<0):
            r0 = r
        print(f'For iteration {i+1} root is {r} and error is {err}')