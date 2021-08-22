#1
a=8
b=9
num=in
x=chislo//10
while x>0:
    x=chislo//10
    y=chislo%10
    if z<y:
        z=y

        print('maximum number is',z)

#5
vir=int(input('input viruchka'))
isder=int(input('input isdergki'))
sootn=0
prib=0
if vir>isder:
    sootn=vir-isder
    prib=sootn/vir
    print('вы работаете с прибылью c рентабельностью',sootn)

else:
    print('вы работаете в убыток')
chislen=int(input('сколько в фирме сотрудников'))
prib=chislen/prib
print('прибыль на одного сотрудника ',prib)

#6

a=input('введите',a)
rez=a
schet=0
b=input('введите',b)
while rez>=b:
    rez=rez+rez/10
    schet=schet+1

print(f'результат достигнут на {schet}:день')




