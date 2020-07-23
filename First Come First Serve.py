# CodeMart is an online shopping platform and it is distributing gift vouchers to its esteemed users. The voucher can be redeemed by providing a fixed amount of shopping credits.Each credit is sent by a user one by one. Since there is a huge rush of people you are required to manage the users on the basis of first come first serve. The user which comes first and has k occurrences of credits is given the voucher first. You are given an array with the id's of the users in chronological order of the credits sent by them. You are required to print the id of the user which will be served first. If no such user meets the condition print "-1".
from collections import OrderedDict
t=int(input())
while(t):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    d = OrderedDict()
    for i in l1:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1

    flag=0
    for i in d:
        if(d[i]==k):
            print(i)
            flag=1
            break
    if(flag==0):
        print(-1)
    t=t-1
