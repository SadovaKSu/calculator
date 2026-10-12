import sys
try:
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))
except ValueError:
    print('Нужно ввести число')
    sys.exit()

operation = input('Выберите операцию (+, -, *, /)')
if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '/':
    if second_number == 0:
        print('На ноль делить нельзя')
    else:
        print(first_number / second_number)
else:
    print('Неизвестная операция')