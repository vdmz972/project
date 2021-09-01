#6

from  math import factorial
def fact():
    for el in count(1):
        yield factorial(el)
        x=0
        for i in fact():
            break
        else:
            x+=1
            print(f"factorial {x}={i}")

