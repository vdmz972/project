#1
def s_calc():

    try:
        r_val = int(input("Первое число "))
        h_val = int(input("Второе число "))
        delen=r_val/h_val
    except ValueError:
        return
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle
    return delen

delen = s_calc()
print(f"Ответ {delen}")



