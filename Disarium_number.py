n=int(input())
t=n
s=0
k=0
for i in str(n):
    s+=1
    m=int(i)**s
    k+=m
if t==k:
    print("True")
else:
    print("False")