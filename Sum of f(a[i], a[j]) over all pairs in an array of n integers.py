# Given an array A of n integers, find the sum of f(a[i], a[j]) of all pairs (i, j) such that (1 <= i < j <= n).
# f(a[i], a[j]):       If | a[j]-a[i] | > 1
#
#                          f(a[i], a[j]) = a[j] - a[i]
#
#                          Else  if | a[j]-a[i] | <= 1
#
#                          f(a[i], a[j]) = 0

t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    s=0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if(abs(l1[j]-l1[i])>1):
                s=s+(l1[j]-l1[i])
    print(s)
    t=t-1
