# Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
# An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
# Note: There may be multiple peak element possible, in that case you may return any valid index (0 based indexing).
def peakElement(arr, n):
    # Code here
    return arr.index(max(arr))
