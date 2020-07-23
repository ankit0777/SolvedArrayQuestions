# Given a word S and a text C. Return the count of the occurences of anagrams of the word in the text.
from collections import Counter
t=int(input())
while t>0:
    s=input()
    text=input()
    count=0
    for i in range(len(s)-len(text)+1):
        if Counter(s[i:len(text)+i])==Counter(text):
            count+=1
    print(count)
    t-=1
