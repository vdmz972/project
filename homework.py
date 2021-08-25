#5
my_list=[9,8,8,7,5,6,4,]
new_number=float(input("Введите элемент рейтинга"))
i=0
for n in my_list:
    if new_number<=n:
        i+=1
    else:
        break
        my_list.insert(i,new_number)
        print(my_list)




