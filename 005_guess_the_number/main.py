import random

random_number = random.randint(1, 100)
print("Я загадал число от 1 до 100.")
tries = 0
while True:
    user_guess = int(input("Твоя попытка: "))
    if user_guess > 100 or user_guess < 1:
        print("Введённое число вне заданного диапазона")
        continue
    tries += 1
    if user_guess == random_number:
        print(f"Верно! Число угадано за {tries} попытки.")
        break
    if user_guess > random_number:
        print("Загаданное число меньше.")
    elif user_guess < random_number:
        print("Загаданное число больше.")
    if abs(user_guess - random_number) <= 5:
        print("Очень близко!")
    elif 5 < abs(user_guess - random_number) <= 15:
        print("Тепло")
    else:
        print("Холодно")