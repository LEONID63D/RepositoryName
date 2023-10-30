disk = 1.44 # Мбайта

nsymb = 25
nstr = 50
npage = 100
onesymb = 4 # Байта

one_book = (onesymb * nsymb * nstr * npage) / (1024 ** 2) # Вес книги в Мбайтах
nbooks = disk // one_book
print("Количество книг, помещающихся на дискету:", int(nbooks))
