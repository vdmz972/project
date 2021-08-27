#2
def my_sum(arg1,arg2):
 return arg1,arg2
a=["имя", "фамилия", "год рождения", "город проживания", "email", "телефон"]
i=0
b=[]
z=''

while i<6:
 z=str(input (a[i]))
 b.insert(i, z)
 i=i+1

'''i=0
while i<6:
 print(a[i],':',b[i])
 i+=1

'''
i=0

while i<6:
 arg1=a[i]
 arg2=b[i]
 print({arg1,arg2})
 i+=1


my_sum(1,2)







