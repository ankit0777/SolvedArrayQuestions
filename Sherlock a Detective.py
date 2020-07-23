# Sherlock is a famous detective. This time he's working to catch a team of gangsters. Sherlock knows that the head of gangsters will be caught if he catches his underlings. The gangsters work under a hierarchical system. Each member reports exactly to one other member of the town. It's clear that there are no cycles in their reporting system.There are N people in the town, for simplicity indexed from 1 to N, and Sherlock knows who each of them report to. Member i reports to member Ai, and head of Gangsters does not report to anybody. Sherlock wants to find the members to whom nobody reports as these members could help him bring down the organization.
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    d={}
    for i in range(len(l1)):
        if(l1[i] not in d):
            d[l1[i]]=1
    for i in range(1,n+1):
        if i not in d:
            print(i,end=" ")
    print('\t')
    t=t-1
