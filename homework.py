#4
def my_func(x,y):
 try:
    res=x**y
 except TypeError:
    return  "Положительное х и целое отрицательное у"
 return res
 print(my_func(3,4,-1))


