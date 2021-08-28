#3

def my_func(num1,num2,num3):
    my_list=[num1,num2,num3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Только цифры"
    print(my_func(6,8,11))
