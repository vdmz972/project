#1
#!/usr/bin/python

f = open('text.txt', 'w')
line = input('Введите текст \n')
while line != '':
    f.writelines(line)
    line = input('Введите текст \n')


print(f'Ввод завершен')
f.close()
f = open('text.txt', 'r')
content = f.readlines()
print(f'Вы ввели{content}')
f.close()


