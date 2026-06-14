x = [0.5,1.5,3.0,5.0,6.5,8.0]
y = [1.625,5.875,31.0,131.0,282.125,521.0]
n = len(x)
d = [[0 for _ in range(n)]for _ in range(n)]
xp = float(input("Enter the value at which the function is to be interpolated: ", ))
for i in range(n):
    d[i][0] = y[i]
    for j in range(1,n):
        for i in range(n-j):
            d[i][j] = (d[i+1][j-1]-d[i][j-1])/(x[i+j]-x[i])
            if(d[i][j]<1e-6):
                d[i][j]=0
print("Difference table:\n")
for row in d:
    print(row)
result = d[0][0]
term = 1
for i in range(1,n):
    term*=(xp-x[i-1])
    result+=(d[0][i])*term
print("The value of function at given x is: ",result)
    

