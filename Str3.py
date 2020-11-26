a=str(input())
b=0
if len(a)%2==1:
    b=1
for k in range(0,len(a)//2+b):
    print(k*' '+f"{a[k:(len(a)-k)]}"+k*' ')