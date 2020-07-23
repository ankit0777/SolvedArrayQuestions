# Given an array which contains all elements occurring k times, but one occurs only once. Find that unique element.
t=int(input())
while(t):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    d={}
    for i in l1:
        if(i not in d):
            d[i]=1
        else:

            d[i]=d[i]+1
    for i in d:
        if(d[i]==1):
            print(i)
            break
    t=t-1
