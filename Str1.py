a=str(input("Cuvantul este "))
b=str(input("Litera este "))
for k in range(0, len(a)):
    print(f"{a[:k]}{b}{a[k+1:]}")