
# Модуль импортирования данных
# Для работы с комплексными и рациональными числами возможно
# импортировать классы fraction и cmath


from fractions import Fraction
import cmath

def get_value():
    value = input('Введите число  ')
    try:
        value = Fraction(value)
        return value
    except ValueError:
        value = complex(value)
        return value

def get_operations():
    operations = input('Введите операцию  ')
    return operations

def get_result(result):
    print(f'Ответ: {result}')
