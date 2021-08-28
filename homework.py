#5
def sum():
s=0
while True:
    in_list=input('Введите число,q для выхода').split()
    for num in in_list:
        if num.lower()=="q":
            return s
        else:
            try:
                s+=int(num)
            except ValueError:
                print('Для выхода нажмите q')
                print(f"Сумма ={s}")

                print(sum())




