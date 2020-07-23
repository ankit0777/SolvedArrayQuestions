# Given an array of elements which is first increasing and then may be decreasing, find the maximum element in the array.
# Note: If the array is increasing then just print then last element will be the maximum value.

t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    print(max(l1))
    t=t-1
