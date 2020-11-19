d=""
m=int(input("Introduceti un nr "))
n=int(input("Introduceti un nr "))
for x in range(1, n):
    if m**x==n:
        d="Da"
if d=="Da":
    print(d)
else:
    print("Nu")
    

