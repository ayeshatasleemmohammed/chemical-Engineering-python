A = [[2,4,-2],[4,9,-3],[2,-3,7]]
B = [[2],[8],[10]]
agm = []
n = len(A)
def f(x,y):
    X = [0]*n
    for i in range(n):
     agm.append(x[i]+y[i])
    print("The agumented matrix is:\n")
    for row in agm:
       print (row)
    for i in range(n):
       for j in range(i+1,n):
          s = agm[j][i]/agm[i][i]
          for k in range(i,n+1):
             agm[j][k] = agm[j][k]-(s*agm[i][k])
    print("The upper triangular matrix is:\n")
    for row in agm:
       print(row)
    for i in range(n-1,-1,-1):
       u =0
       for j in range(i+1,n):
          u+=agm[i][j]*X[j]
       X[i]= (agm[i][n]-u)/agm[i][i]
    print("solution matrix is:\n")
    for row in X:
       print(row)
f(A,B)
        
    