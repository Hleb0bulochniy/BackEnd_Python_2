'''
Вторая лабораторная, где надо показать знания, связанные с операторами преобразования
 и присваивания, условными операторами, операторами цикла, переменными, функциями
'''
def main():
    '''Функция main, содержащая вызовы остальных функций'''
    print("Типы")
    types()
    print("Операции присваивания")
    assignment_operators()
    print("Операции преобразования")
    conversion_operators()
    print("операторы циклов и условий")
    conditions_and_cycles(10)


def types():
    '''Разбор типов данных'''
    bool_variable = True
    int_variable = 12
    float_variable = 12.34
    complex_variable = 3+4j
    #комплексные числа нужны для сложных физических и математических рассчетов
    str_variable = "Lorem Ipsum"

    bool_variable = 14
    #переменные типизируются динамически
    print(bool_variable)
    print("")

    int_variable = 0b1100
    #можно записать целочисленное значение в разных системах:
    #двоичной 0b
    #восьмеричной 0o
    #и шестнадцатиричной 0x системах
    print(int_variable)
    print(f"{int_variable:0b}")
    #можно использовать спецификатор, чтобы перевести число в нужную систему
    #для использования спецификатора строка должна быть форматируемой
    print("")

    float_variable = 1234e-2
    #дробное число можно определять в экспоненциальной записи
    print(float_variable)
    print(round(float_variable))
    #числа можно округлять
    float_variable = 135e-1
    print(round(float_variable))
    #если округление одинаково далеко от большего и меньшего, то округляется к ближайшему четному
    float_variable = 12345e-3
    print(round(float_variable, 2))
    #в округлении можно будет указать, сколько знаков должно быть после запятой
    print("")

    print(complex_variable.real)
    print(complex_variable.imag)
    #у комплесных чисел можно выделить действительную и мнимую части
    print("")

    str_variable = 'hello'
    str_variable = "hello"
    #можно использовать как одну, так и две кавычки
    str_variable = ("hello "
                    "world")
    #ввод можно разделить на несколько строк с помощью скобок
    str_variable = '''hello
my
name
is
Danya'''
    #многострочный текст можно записывать через тройные кавычки без специальных символов
    str_variable = "Hello!\nI\'m your \"friend\""
    print(str_variable)
    #можно использовать различные спец. символы:
    # \\: позволяет добавить внутрь строки слеш
    # \': позволяет добавить внутрь строки одинарную кавычку
    # \": позволяет добавить внутрь строки двойную кавычку
    # \n: осуществляет переход на новую строку
    # \t: добавляет табуляцию (4 отступа)
    str_variable = f"Age: {int_variable}"
    print(str_variable)
    #в строку можно вставлять различные значения
    print("")


def assignment_operators():
    '''Функция показывает операторы присваивания'''
    a = 0
    print(a)
    a += 2
    print(a)
    a -= 1
    print(a)
    a *= 14
    print(a)
    a /= 2
    print(a)
    a //= 2
    print(a)
    a **= 2
    print(a)
    a %= 2.5
    print(a)
    #стандартные операции
    print()

    a = 0b101
    b = 0b100
    a &= b
    print(a)
    a = 0b101
    b = 0b10
    a |= b
    print(a)
    a = 0b101
    b = 0b100
    a ^= b
    print(a)
    #логические операции
    print()

    a = 16
    a >>= 2
    print(a)
    a <<= 1
    print(a)
    #операции сдвига
    print()


def conversion_operators():
    '''Функция показывает операторы преобразования'''
    print(int(12.34))
    print(float(1))
    print(str(123))
    print(bool(0))
    print()


def conditions_and_cycles(amount):
    '''Функция показывает условние операторы и циклы'''
    number = 0
    while number <= amount:
        number += 1
        if number == 5.5:
            print(f"Цикл прерван прерван на числе {number}")
            break
    else: print("работа цикла завершениа успешно")
    #else выполняется после завершения цикла, когда условие уже не выполняется
    print()

    for i in range(0, amount, 3):
        print(i)
        if i %2 != 1:
            continue
        elif i == 3:
            print ("цифра 3")
        print(f"i нечетная {i}")
    #можно поставить шаг итерации при объявлении
    #continue игнорирует дальнейшие инструкции и перескакивает к следующей итерации
    print()

    a = 5
    print(a==5)
    print(a!=5)
    print(a>=5)
    print(a<=4)
    print(a>5)
    print(a<5)
    print()
    #операции сравнения

    print(a>5 or a<5)
    print(a>4 and a<6)
    print(not True)
    print()
    #логические операции

    a = "one two three four"
    print("three" in a)
    print()
    #оператор in


main()
