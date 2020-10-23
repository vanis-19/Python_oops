a=[1,2,3,4,5,6]
target=4
for i in range(0,len(a)-1):
    for j in range(i+1, len(a)):
        if(a[i]+a[j]==target):
            print([i,j])

