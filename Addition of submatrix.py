# Given a matrix C of size N x M. You are given position of submatrix as X1, Y1 and X2, Y2 inside the matrix. Find the sum of all elements inside that submatrix.
import numpy as np
t=int(input())
while(t):
    n,m=map(int,input().split())
    l1=[]
    entries = list(map(int, input().split()))

    x1,y1,x2,y2=map(int,input().split())
    matrix = np.array(entries).reshape(n, m)
    sum=0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            sum=sum+matrix[i][j]
    print(sum)

    t=t-1
