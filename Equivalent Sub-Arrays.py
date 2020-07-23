# Given an array of n integers. Count the total number of sub-array having total distinct elements same as that of total distinct elements of the original array.
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=[]
    for i in l1:
        if(i not in l2):
            l2.append(i)
    n1=len(l2)

    c=0
    for i in range(n):
        for j in range(i,n):
            if len(set(l1[i:j+1]))==n1:
                c+=1
    print(c)

    t=t-1
