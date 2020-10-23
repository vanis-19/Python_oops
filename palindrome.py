n=121
s=0
while n>0:
    rem=n%10
    s=s*10+rem
    n=n//10

if s==n:
    print('palindrome')
else:
    print('not palindrome')    