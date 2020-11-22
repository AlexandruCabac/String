a=str(input())
b=0
if(len(a)==13):
    b=1
for i in range(0,len(a)):
    if(b==0):
        break
    if(ord(a[i])<48 or ord(a[i])>57):
        b=0
if(b==1):
    print("Totul e ok")
else:
    print("CNP-ul persoanei este incorect")