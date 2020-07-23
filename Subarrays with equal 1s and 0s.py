# Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.
def countSubarrWithEqualZeroAndOne(arr, N):
    #Your code here
    res=0
    for i in range(2,N+1,2):
        for j in range(0,N-i+1):
            if(arr[j:j+i].count(0)==arr[j:j+i].count(1)):
                res=res+1
    return res
