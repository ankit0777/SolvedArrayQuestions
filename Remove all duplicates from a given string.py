# Given a string which may contains lowercase and uppercase chracters. The task is to remove all  duplicate characters from the string and print the resultant string.  The order of remaining characters in the output should be same as in the original string.
#code
t=int(input())
while(t):
    s=input()
    l1=[]
    for i in s:
        if i not in l1:
            l1.append(i)
    p="".join(l1)
    print(p)
    t=t-1
