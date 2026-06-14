A = [[10,1],[1,10]]
B =[11,11]
iterations = int(input("Enter the number of iterations: ", ))
def f(x,y):
    n = len(x)
    X_new =[0]*n
    X_old = [0]*n
    for iter in range(iterations):
       for i in range(n):
          u = 0
          for j in range(n):
            if(j!=i):
                u+=x[i][j]*X_old[j]
          X_new[i]=(y[i]-u)/x[i][i]
          X_old = X_new.copy()
    print("The solution matrix is:\n")
    for row in X_old:
        print(row)
f(A,B)
