#1
a=8
b=9
num=int(input('input number'))
str=input('input word')
print (a,b,str,num)
#2
time=int(input('input time in sec'))
hour=int(time//3600)
sec=int(time%60)
minutes=int(time//60)
print(f"{hour:.2f}:{minutes:.2f}:{sec:.2f}")
#3
n=input('input number')
n1=n+n
n2=n+n+n
n3=int(n)+int(n1)+int(n2)
print(n3)
#4
chislo=int(input('input number'))
z=0
y=0
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




