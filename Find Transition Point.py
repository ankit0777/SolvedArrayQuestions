# You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. The transition point is a point where "0" ends and "1" begins (0 based indexing).
# Note that, if there is no "1" exists, print -1.
# Note that, in case of all 1s print 0.
def transitionPoint(arr, n):
    #Code here
    flag=0
    if(n==0):
        return -1
    else:
        for i in range(n):
            if(arr[i]==1):
                pos=i
                flag=1
                break
        if(flag==1):
            return pos
        else:
            return -1
