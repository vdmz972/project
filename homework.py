#5
from  functools import reduce
def my_list(el1,el2):
    return el1*el2
new_list=[el for el in range(100,1001,2)]
print(f"\n{new_list}\n Повторение номеров \n{reduce(my_list(,new_list))}")




