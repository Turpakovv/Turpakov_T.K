# #У вас имеется информационный объем дискеты, равный 1,44 Мб, а также параметры книги, такие как количество страниц, число строк на странице и количество символов в строке.
# Ваша задача — рассчитать, сколько одинаковых книг можно поместить на дискету, и вывести результат на экран.

# Информационный объем дискеты равен 1,44 Мб.
# Количество страниц в книге - 100.
# Число строк на странице - 50.
# Количество символов в строке - 25.
# Для хранения кода одного символа нужно 4 байта.

disk_capacity_mb = 1.44
pages_in_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 Кб = 1024 * 1024 байт
book_size_bytes = pages_in_book * lines_per_page * chars_per_line * bytes_per_char
number_of_books = int(disk_capacity_bytes // book_size_bytes)
print("Количество книг, помещающихся на дискету:", number_of_books)