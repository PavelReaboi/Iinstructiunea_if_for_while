n=int(input("Introduceti un nr "))
s1=0
s2=0
for a in range(1, n+1):
    s1+=a**3
for a in range(1, n+1):   
    s2+=a
    s2**=2
if s1>s2:
    print("Suma lui s1 (",s1,") este mai mare decit suma lui s2 (",s2,")")
if s1<s2:
    print("Suma lui s2 (",s2,") este mai mare decit suma lui s1 (",s1,")")
elif s1==s2:
    print("Suma lui s1 (",s1,") si suma lui s2 (",s2,") sunt egale")

