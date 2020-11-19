a=int(input("Introduceti un nr "))
b=int(input("Introduceti un nr "))
c=int(input("Introduceti un nr "))
if (a<0 or b<0 or c<0):
     print("Nu e triunghi")
elif (a==b) and (a!=c) :
     print("Triunghi isoscel ")
elif (a==c)and (c!=b):
     print("Triunghi isoscel ")
elif (b==c) and (a!=c):
     print("Triunghi isoscel ")
elif (a==b and b==c and a==c):
     print("Triunghi echilateral")
else:
     print("Triunghi scalen")