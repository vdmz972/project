#4
import random
my_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

len_my_list=(len(my_list))
new_list=[]
i=0
p=0
my_dict = dict()

l=set()
while i<=13:
  l.add(my_list[i])
  i+=1
new_list = [el for el in my_list if el % 2 == 0]
print(l)


