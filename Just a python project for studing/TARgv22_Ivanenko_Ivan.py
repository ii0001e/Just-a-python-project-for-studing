from math import *

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))
S=a**2
print("Ruudu pindala - ",S)
P=4*a
print("Ruudu ümbermõõt - ",P)
di_1=round(a*sqrt(2),2)
print("Ruudu diagonaal - ",di_1,"\n")
######################################
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S_1=b*c
print("Ristküliku pindala - ",S_1)
P=2*(b+c)
print("Ristküliku ümbermõõt - ",P)
di_2=round(sqrt(b**2+c**2),2)
print("Ristküliku diagonaal - ",di_2,"\n")
#######################################
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi läbimõõt - ",d)
S_2=round(pi*r**2,2)
print("Ringi pindala - ",S_2)
Cp=round(2*pi*r,2)
print("Ringjoone pikkus - ",Cp)