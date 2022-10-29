n=int(input())
s1=s=0
t=n
while n>0:
    k=n%10
    s=s*10+k
    n=n//10
a=s**2
while a>0:
    d=a%10
    s1=s1*10+d
    a=a//10
if t**2==s1:
    print('True')
else:
    print('False')
    
    
    