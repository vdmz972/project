#2
a=["имя", "фамилия", "год рождения", "город проживания", "email", "телефон"]
i=0
b=[]
z=''

while i<6:
 z=str(input (a[i]))
 b.insert(i, z)
 i=i+1

i=0
while i<6:
 print(a[i],':',b[i])
 i+=1







