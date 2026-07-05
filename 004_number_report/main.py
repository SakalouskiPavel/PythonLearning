print("Введи положительное целое число: ")
number = int(input())
sum_of_numbers = 0
sum_of_squares = 0
even_numbers_count = 0

for i in range(1, number + 1):
    print(f"{i} -> {i ** 2}")
    sum_of_numbers += i
    sum_of_squares += i ** 2
    if i % 2 == 0:
        even_numbers_count += 1
print(f"Сумма чисел: {sum_of_numbers}")
print(f"Сумма квадратов: {sum_of_squares}")
print(f"Количество чётных чисел: {even_numbers_count}")
