# Given an array containing positive and negative numbers. The array represents checkpoints from one end to other end of street. Positive and negative values represent amount of energy at that checkpoint. Positive numbers increase the energy and negative numbers decrease. Find the minimum initial energy required to cross the street such that Energy level never becomes 0 or less than 0.
t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    s=0
    flag=0
    for i in l1:
        s=s+i
        if(s<0):
            s=s-1
            flag=1
            break;
    if(flag==0):
        print(1)
    else:
        print(abs(s))
            
