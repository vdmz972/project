#6

def int_func():
    for word in input("Введите слово из маленьких латинских букв:\n").split():
        chars=0
        for char in word:
            if 97<=ord(char)<=122:
                chars+=1
                print(word.title()if chars==len(word) else f"{word}Только маленькие английские буквы")

                int_func()




