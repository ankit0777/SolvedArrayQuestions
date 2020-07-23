# Given an array of size N consisting of only 0's and 1's ,which is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. You have to find  the count of all the 0's.
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    print(l1.count(0))

    t=t-1
    
