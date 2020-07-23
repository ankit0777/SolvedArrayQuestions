# Monu lives in a society which is having high rise buildings. This is the time of sunrise and monu wants see the buildings receiving the sunlight. Help him in counting the number of buildings recieving the sunlight.
# Given an array H representing heights of buildings. You have to count the buildings which will see the sunrise (Assume : Sun rise on the side of array starting point).
#code
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=[]
    c=1
    l2.append(l1[0])
    p=0
    for i in range(1,n):
        if(l1[i]>l2[p]):
            l2.append(l1[i])
            p=p+1
            c=c+1
    print(c)
    t=t-1
