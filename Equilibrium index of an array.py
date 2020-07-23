# Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
# Given an array, your task is to find the index of first Equilibrium point in the array.
# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
    # Code here
    # for i in range(1,n):
    #     if(sum(a[0:i])==sum(a[i+1:n])):
    #         return i
    # return -1
    sum1=0
    r=a[0]
    for i in range(1,n):
        sum1=sum1+a[i]
    for i in range(1,n):
        sum1=sum1-a[i]
        if sum1==r:
            return i
        else:
            r=r+a[i]
    return -1

    
