#3

el=int(input('номер месяца'))

seasons_list=['december','january','february','march','april','may','june','julay','august','september','october','november']
month=(seasons_list[el])

my_dict = {7:"summer", 8:"summer", 9:"summer",10:"autumn",
           11:"autumn",12:"autumn",1:"winter",2:"winter",3:"winter",4:"spring",5:"spring",6:"spring"
           }
print(el)
season=my_dict.setdefault(el)

print(f"месяц:{month},время года:{season}")



