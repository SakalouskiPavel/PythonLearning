def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return None
    return first_number / second_number


def power(first_number, second_number):
    return first_number ** second_number


def main():
    operations = ["+", "-", "*", "/", "**", "exit"]
    while True:
        user_input = input("Операция (+, -, *, /, ** или exit): ")
        if user_input in operations:
            if user_input == "exit":
                print("До встречи!")
                break

            first_number = float(input("Первое число: "))
            second_number = float(input("Второе число: "))
            if user_input == "+":
                print(f"Результат: {add(first_number, second_number)}")
            elif user_input == "-":
                print(f"Результат: {subtract(first_number, second_number)}")
            elif user_input == "*":
                print(f"Результат: {multiply(first_number, second_number)}")
            elif user_input == "/":
                division_result = divide(first_number, second_number)
                if division_result is None:
                    print("На ноль делить нельзя")
                    continue
                print(f"Результат: {division_result}")
            elif user_input == "**":
                print(f"Результат: {power(first_number, second_number)}")
        else:
            print("Неизвестная операция.")



if __name__ == "__main__":
    main()
