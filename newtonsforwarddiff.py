x = [0.1,0.2,0.3,0.4,0.5]
y = [1.40,1.56,1.76,2.00,2.28]
n = len(x)
d = [[0 for _ in range(n)]for _ in range(n)]
xp = float(input("Enter x at which function's value is to be found:"))
h = x[1]-x[0]
s = (xp-x[0])/h
for i in range(n):
    d[i][0] = y[i]
for j in range(1,n):
    for i in range(n-j):
        d[i][j]=d[i+1][j-1]-d[i][j-1]
        if(d[i][j]<1e-6):
            d[i][j]=0
print("Difference table:\n")
for row in d:
    print(row)
result = d[0][0]
s_fact = 1
fact =1
for i in range(1,n):
    s_fact*=(s-(i-1))
    fact*=i
    result+=(d[0][i]*s_fact)/fact
print("The value of function at given x is: ",result)
