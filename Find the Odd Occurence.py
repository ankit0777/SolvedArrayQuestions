# Given an array of positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the number.
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    d={}
    for i in l1:
        if(i not in d):
            d[i]=1
        else:
            d[i]=d[i]+1
    flag=0
    for i in d:
        if(d[i]%2==0):
            continue
        else:
            print(i)
            flag=1
            break
    if(flag==0):
        print(0)
    t=t-1
            
