n=int(input())
s=0
t=1
while n>0:
    r=n%10
    s+=r
    t*=r
    n=n//10
print(t-s)