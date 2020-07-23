# Given an array of integers, and an integer  ‘K’ , find the count of pairs of elements in the array whose sum is equal to 'K'.
t=int(input())
while(t):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if(l1[i]+l1[j]==k):
                c=c+1

    print(c)
    t=t-1
