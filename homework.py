#6

from  itertools import count,cycle
my_count=count(7)
my_cyrcle=cycle("abc")
for _ in range(5):
    print("(my_count,my_cyrcle)=({},{})".format(next(my_count),next(my_cyrcle)))
    


