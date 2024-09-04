x='''
Welcome to JOSHAN'S Linear Motion  Calculator!!
 ECE

'''
print(x)
y='''
What do you want to calculate?
1-Velocity of the object
2-Accleration of the object
3-Momentum of the object
4-Force of the object
'''
print(y)
a={1:"velocity of the object",2:"accleration of the object",3:"momentum of the object",4:"force of the object"}
b=int(input("choose the number for which you want to calculate:"))
c=a[b]
z='''   '''
print(z)
print(" You have selected ",c)
w='''   '''
print(w)
D=float(input("Enter the value of displacement(in meter):"))
T=float(input("Enter the value of time(in sec):"))
M=float(input("Enter the value of mass(in kg):"))
velocity=round(D/T,2)
accleration=round(velocity/T,2)
momentum=round(M*velocity,2)
force=round(M*accleration,2)
q='''   '''
print(q)
if b==1:
      print("VELOCITY IS EQUAL TO",velocity,"meter per second")
elif b==2:
      print("ACCLERATION IS EQUAL TO",accleration,"meter per second square")
elif b==3:
      print("MOMENTUM IS EQUAL TO",momentum,"kilogram metre per second")
elif b==4:
      print("FORCE IS EQUAL TO",force,"Newton")
m='''   '''
print(m)
print("THANK YOU")

