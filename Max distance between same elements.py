# Given an array with repeated elements, the task is to find the maximum distance between two occurrences of an element.

def maxDistance(arr, n):
    # Code here
    d={}
    for i in range(n):
        if arr[i] not in d:
            l=[]
            l.append(i)
            d[arr[i]]=l
        else:
            d[arr[i]].append(i)
    max=0
    for i in d:
        a=d[i][len(d[i])-1]-d[i][0]
        if a>max:
            max=a
    return max
