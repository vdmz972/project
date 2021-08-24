#4
stroka=str(input("Введите строку"))



razd=stroka.split(' ')



schet=len(razd)
i=0
a=0
while schet>0:
    a = razd[i]
    print(a)
if len(razd[i])<10:
     print(i+1,razd[i])
else:
     print(a[1:10])
i=i+1
schet=schet-1



