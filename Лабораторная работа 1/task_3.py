# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44 * 1024 * 1024 #Объем дискеты в байтах

count_page = 100
count_string = 50
count_character = 25
volume_character = 4

volume_string = count_character * volume_character
volume_page = volume_string * count_string
volume_book = volume_page * count_page

count_book = int(volume_disk // volume_book)

print("Количество книг, помещающихся на дискету:", count_book)
