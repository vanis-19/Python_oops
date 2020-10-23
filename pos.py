'''nums=[5,7,7,8,8,10]
target=8
for i in range(len(nums)-1):
    if(nums[i]==target):
        print(i, end=' ')'''


l=[5,7,7,8,8,10]
target=8
i=0
j= len(l)-1
while(i<=j):
    if l[i]==target and l[j]==target:
        print([i,j])
    elif l[i]==target and l[j]!= target:
        j-=1
    elif l[j]==target and l[i]!= target:
        i+=1
    else:
        i+=1
        j-=1
print([-1,-1])