A = [[10,1],[1,10]]
B =[11,11]
iterations = int(input("Enter the number of iterations: ", ))
def f(x,y):
    n = len(x)
    X =[0]*n
    for iter in range(iterations):
       for i in range(n):
          u = 0
          for j in range(n):
            if(j!=i):
                u+=x[i][j]*X[j]
          X[i]=(y[i]-u)/x[i][i]
    print("The solution matrix is:\n")
    for row in X:
        print(row)
f(A,B)

