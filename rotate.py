l=[1,2,3,4,5]
n=2
l=l[n+1:]+l[:n+1]
l=l[-n:]+l[:-n]
print(l)
