# Given an array of integers. Check whether it contains a triplet that sums up to zero.
''' Your task is to returns 1 if there is triplet with sum equal
    to 0 present in arr[], else return 0'''
from itertools import combinations
def findTriplets(arr,n):
    #code here
    arr.sort()
    for i in range(n):
        j=i+1
        k=n-1
        while(j<k):
            s=arr[i]+arr[j]+arr[k]
            if(s==0):
                return 1
            elif(s>0):
                k=k-1
            else:
                j=j+1
    return 0
