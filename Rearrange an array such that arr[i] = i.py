# Given an array of size N that has elements ranging from 0 to N-1. All elements may not be present in the array. If element is not present then there will be -1 present
#
# in the array. Rearrange the array such that A[i] = i, and if i is not present, display -1 at that place.

t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    d={}
    for i in range(n):
        if((i in l1) and (i not in d)):
            d[i]=i
        elif((i in l1) and (i in d)):
            d[i]=d[i]+1
        else:
            d[i]=-1
    for i in d:
        print(d[i],end=" ")
    print('\t')
    t=t-1
