# Given an array with positive number the task to find the largest subsequence from array that contain elements which are Fibonacci numbers.
import math
def check(p):
    sr = math.sqrt(p)


    return ((sr - math.floor(sr)) == 0)

t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    for i in l1:
        if(check(5*i*i+4) or check(5*i*i-4)):
            print(i,end=" ")
    print('\t')
    t=t-1
