# Given two sorted arrays of size m and n of distinct elements. Given a value x. The problem is to count all pairs from both arrays whose sum is equal to x.
# # Note: The pair has an element from each array.
while(t):
    n1,n2=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x=int(input())
    l1=list(set(l1))
    l2=list(set(l2))

    c=0
    for i in l1:
        if(x-i in l2):
            c=c+1
    print(c)
    t=t-1
