q=str(input())
x=len(q)
a=b=c=0
for i in range(0,x):
    if(ord(q[i])>=65 and ord(q[i])<=96):
        a+=1
    elif(ord(q[i])>=48 and ord(q[i])<=57):
        b+=1
    elif(ord(q[i])>=40 and ord(q[i])<=47)or(ord(q[i])>=58 and ord(q[i])<=62)or(ord(q[i])>=91 and ord(q[i])<=94)or(ord(q[i])>=123 and ord(q[i])<=125)or(ord(q[i])>=239 and ord(q[i])<=251)or ord(q[i])==33 or ord(q[i])==37:
        c+=1
print(a,b,c)