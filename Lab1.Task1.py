# Замена пропущенного элемента средним арифметическим
# Описание:
# У вас есть список чисел, в котором один из элементов случайно пропущен.
# Ваша задача — найти пропущенный элемент и заменить его средним арифметическим всех остальных элементов списка.
# При расчете суммы для среднего арифметического берутся все числа, кроме пропуска.
# А для расчёта количества — все элементы, включая пропуск.

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_sum = sum(num for num in numbers if num is not None)
count = len(numbers)
average = total_sum / count
numbers[numbers.index(None)] = average
print("Измененный список:", numbers)