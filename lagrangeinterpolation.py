x = [0,1,3]
y = [1,3,55]
n = len(x)
xp = float(input("Enter the value of x at whcih function is to be interpolated: "))
result = 0
for i in range(n):
    term =y [i]
    for j in range(n):
       if(j!=i):
        term*=(xp-x[j])/(x[i]-x[j])
    result += term
print(result)
    