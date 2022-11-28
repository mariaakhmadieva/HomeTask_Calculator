
# Модуль импортирования данных

def get_value():
    value = input('Введите число: ')
    if "j" in value:
        return complex(value)
    return float(value)

def get_operations():
    operations = input('Введите операцию: ')
    return operations

def get_result(result):
    print(f'Ответ: {result}')
