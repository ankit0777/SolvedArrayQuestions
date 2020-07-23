# Given a set of N nuts of different sizes and N bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.
#
# Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.

t=int(input())
while(t):
    n=int(input())
    l1=list(input().split())
    l2=list(input().split())
    l3=['!', '#', '$', '%', '&' ,'*','@', '^', '~' ]
    for i in range(len(l3)):
        if(l3[i] in l1 ):
            print(l3[i],end=" ")
    print("\t")
    for i in range(len(l3)):
        if(l3[i] in l1 ):
            print(l3[i],end=" ")
    print("\t")
    t=t-1
