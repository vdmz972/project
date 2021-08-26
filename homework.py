#2
a=["имя", "фамилия", "год рождения", "город проживания", "email", "телефон"]
i=0
b=0
z=0

while i<6:
 z=input(a[i])
 b={a[i]:z[i]}
 i=i+1

print(z)


a=["имя", "фамилия", "год рождения", "город проживания", "email", "телефон"]

global c,b,i
c=0
i=0
b=''
while i<6:
 key=input ('введите')
 b[i]=key
 i=i+1

print(b)





