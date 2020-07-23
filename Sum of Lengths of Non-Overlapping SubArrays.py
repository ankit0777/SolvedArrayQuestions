# Given an array of N elements, you are required to find the maximum sum of lengths of all non-overlapping subarrays with K as the maximum element in the subarray.
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    k=int(input())
    z=0
    c=0
    while(c<n):
        l2=[]
        for i in range(c,n):
            if(l1[i]<=k):
                l2.append(l1[i])
            else:
                break

        if(len(l2)>0 and (k in l2)):
            c=c+len(l2)
            z=z+len(l2)
        else:
            c=c+1
    print(z)
    t=t-1
