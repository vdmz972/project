#4
stroka=str(input("Введите строку"))



razd=stroka.split(' ')



schet=len(razd)
i=0
a=0
while schet>0:
    a = razd[i]

    if len(razd[i])<10:
     print(i+1,razd[i])
     i = i + 1
     schet = schet - 1
    else:
     print(i+1,a[1:10])
     i=i+1
     schet=schet-1



