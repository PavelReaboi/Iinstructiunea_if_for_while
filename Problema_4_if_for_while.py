from fractions import Fraction
c=int(input("Introduceti un nr pentru numitor: "))
b=int(input("Introduceti un nr pentru numarator: "))
g=int(input("Introduceti un nr pentru numitor: "))
d=int(input("Introduceti un nr pentru numarator: "))
x=Fraction(b, c)
y=Fraction(d, g)
a=x+y
print("Adunarea fractiilor este egal cu ", a)
b=x*y
print("Inmultirea fractiilor este egal cu ", b)
