import numpy as np



x = np.arange(5)
h = np.diff(x)
n = 5
A = np.zeros((n,n))
A[0,0] = 1.0
for i in range(n-1):
    if i != (n-2):
        A[i+1 , i+1] = 2.0 * (h[i] + h[i+1])
    A[i+1,i] = h[i]
    A[i,i+1] = h[i]
print(A)





