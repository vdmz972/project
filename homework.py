#2

my_file = open('text.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('text.txt', 'r')
content = my_file.readlines()
print(f'в файле - {len(content)} строк')
my_file = open('text.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'В {i + 1} - ой строке {len(content[i])} символов')
my_file = open('text.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Всего слов - {len(content)}')
my_file.close()








