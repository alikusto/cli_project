# calc.py

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"


def calculator():
    print("Простой калькулятор CLI")
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычетание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Введите номер операции (1/2/3/4/5): ")

        if choice == "5":
            print("Выход из калькулятора.")
            break

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Введите числа корректно.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        else:
            print("Ошибка: Некорректный выбор операции.")
            continue

        print("Результат: {}".format(result))


if __name__ == "__main__":
    calculator()
