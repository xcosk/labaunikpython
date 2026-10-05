#  1 42 разными способами


a1 = 42                     # просто число
a2 = 42.0                   # число с точкой (float)
a3 = int("42")              # число из строки "42"
a4 = int(True) * 42         # True это как 1, поэтому 1 * 42 = 42
a5 = 2 ** 5 + 10            # 2 в степени 5 (=32) плюс 10 = 42
a6 = 6 * 7                  # обычное умножение
a7 = len("a" * 42)          # строка из 42 букв "a", а len() считает её длину
a8 = 84 // 2                # целочисленное деление (84 делим на 2)
a9 = bool(1) + 41           # True (=1) + 41 = 42
a10 = ord("*")              # у символа "*" код в таблице ASCII как раз 42!

print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

# 1.4. Проблема с 0.1 в цикле

# бесконечный цикл, который никогда не завершится, потому что 0.1 нельзя точно представить в двоичной системе
# a = 10
# while a != 0:
#     a -= 0.1

# 1.5. 2 ** z "зависает"

# слишком большим z, например 2 ** 1000000, Python будет пытаться вычислить это число, но оно будет занимать слишком много памяти и времени, что приведет к зависанию программы.
# z = 1
# z <<= 40
# 2 ** z



# 1.6. ++i не является инкрементом


# в python нету i++
# i = 0
# while i < 10:
#     print(i)
#     ++i



# 1.7. (True * 2 + False) * -True


# true и false это 1 и 0 тут и получается так что это просто уровнение
# (True * 2 + False) * -True


# 1.8. Цепочки сравнений


# первое true потму что 10 больше 5 и 1, false потому что единица не больше 1 

# x = 5
# 1 < x < 10
# True

# 1 < (x < 10)
# False



# 2.1. SyntaxError: invalid syntax

# просто некорректная конструкция — питон не понимает, что это значит
# if True
#     print("hello")



# 2.2. SyntaxError: cannot assign to literal

# нельзя присвоить значение самому числу, слева должна быть переменная
# 42 = 5



# 2.3. NameError: name ... is not defined

# используем переменную, которую никогда не создавали
# print(some_undefined_variable)



# 2.4. SyntaxError: unterminated string literal

# забыли закрыть кавычку у строки
# s = "привет



# 2.5. TypeError: unsupported operand type(s) for ...

# нельзя сложить число и строку напрямую
# result = 5 + "5"



# 2.6. IndentationError: expected an indented block

# после двоеточия обязательно должен быть отступ с телом блока
# if True:
# print("hello")



# 2.7. IndentationError: unindent does not match any outer indentation level

# отступы "перепутаны" — не совпадают ни с одним из предыдущих уровней
# def func():
#     x = 1
#         y = 2
#       z = 3



# 2.8. ValueError: math domain error

# нельзя взять квадратный корень из отрицательного числа
# import math
# math.sqrt(-1)



# 2.9. OverflowError: math range error

# результат настолько огромный, что не помещается даже в float
# import math
# math.exp(1000)



# Задание 3 — Арифметика
import random



# 3.1. Умножение на 12 (4 сложения)


def mul12(x):
    a = x + x      # 2x
    b = a + a      # 4x
    c = b + b      # 8x
    d = c + b      # 8x + 4x = 12x
    return d



# 3.2. Умножение на 16 (4 сложения)


def mul16_(x):
    a = x + x      # 2x
    b = a + a      # 4x
    c = b + b      # 8x
    d = c + c      # 16x
    return d



# 3.3. Умножение на 15 (3 сложения, 2 вычитания)


def mul15(x):
    a = x + x      # 2x                       (сложение 1)
    b = a + a      # 4x                       (сложение 2)
    c = b + b      # 8x                       (сложение 3)
    d = x - c      # x - 8x = -7x             (вычитание 1)
    e = c - d      # 8x - (-7x) = 15x         (вычитание 2)
    return e



# 3.4. Исправленный naive_mul + автотестирование


def naive_mul(x, y):
    r = 0
    for i in range(y):
        r = r + x
    return r



# 3.5. fast_mul — умножение "в столбик" (без рекурсии)


def fast_mul(x, y):
    result = 0
    while y > 0:
        if y % 2 == 1:
            result = result + x
        x = x + x
        y = y // 2
    return result



# 3.6. fast_pow — возведение в степень (та же схема, "+" -> "*")


def fast_pow(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result = result * x
        x = x * x
        y = y // 2
    return result



# 3.7. mul16 — умножение 16-битных чисел через четыре 8-битных
#
# x = xh*256 + xl,  y = yh*256 + yl
# x*y = xh*yh*256^2 + (xh*yl + xl*yh)*256 + xl*yl


def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16(x, y):
    xl, xh = x & 0xFF, (x >> 8) & 0xFF
    yl, yh = y & 0xFF, (y >> 8) & 0xFF

    ll = mul_bits(xl, yl, 8)
    lh = mul_bits(xl, yh, 8)
    hl = mul_bits(xh, yl, 8)
    hh = mul_bits(xh, yh, 8)

    return (hh << 16) + ((lh + hl) << 8) + ll



# 3.8. mul16k — алгоритм Карацубы (3 умножения вместо 4)
#
# (xh+xl)*(yh+yl) = xh*yh + xh*yl + xl*yh + xl*yl
# => xh*yl + xl*yh = (xh+xl)*(yh+yl) - xh*yh - xl*yl


def mul16k(x, y):
    xl, xh = x & 0xFF, (x >> 8) & 0xFF
    yl, yh = y & 0xFF, (y >> 8) & 0xFF

    z0 = mul_bits(xl, yl, 8)                          # xl*yl
    z2 = mul_bits(xh, yh, 8)                          # xh*yh
    z1 = mul_bits(xh + xl, yh + yl, 9) - z0 - z2      # xh*yl + xl*yh

    return (z2 << 16) + (z1 << 8) + z0



# 3.9. Генератор программ fast_mul_gen(y)


def fast_mul_gen(y):
    lines = ["def f(x):"]

    if y == 0:
        lines.append("    return 0")
        return "\n".join(lines)

    base_var = "x"
    result_assigned = False
    counter = 0
    y_remaining = y

    while y_remaining > 0:
        if y_remaining % 2 == 1:
            if not result_assigned:
                lines.append(f"    r = {base_var}")
                result_assigned = True
            else:
                lines.append(f"    r = r + {base_var}")
        y_remaining //= 2
        if y_remaining > 0:
            counter += 1
            new_base = f"t{counter}"
            lines.append(f"    {new_base} = {base_var} + {base_var}")
            base_var = new_base

    lines.append("    return r")
    return "\n".join(lines)



# 3.10. Генератор программ для возведения в степень


def fast_pow_gen(y):
    lines = ["def f(x):"]

    if y == 0:
        lines.append("    return 1")
        return "\n".join(lines)

    base_var = "x"
    result_assigned = False
    counter = 0
    y_remaining = y

    while y_remaining > 0:
        if y_remaining % 2 == 1:
            if not result_assigned:
                lines.append(f"    r = {base_var}")
                result_assigned = True
            else:
                lines.append(f"    r = r * {base_var}")
        y_remaining //= 2
        if y_remaining > 0:
            counter += 1
            new_base = f"t{counter}"
            lines.append(f"    {new_base} = {base_var} * {base_var}")
            base_var = new_base

    lines.append("    return r")
    return "\n".join(lines)



# Автоматическое тестирование всех функций


if __name__ == "__main__":

    # 3.1 - 3.3: простые проверки на фиксированных функциях
    for x in range(-50, 50):
        assert mul12(x) == x * 12
        assert mul16_(x) == x * 16
        assert mul15(x) == x * 15
    print("3.1-3.3: mul12 / mul16_ / mul15 — все тесты пройдены!")

    # 3.4: naive_mul
    for _ in range(1000):
        x = random.randint(-1000, 1000)
        y = random.randint(0, 1000)   # naive_mul рассчитан на неотрицательные y
        assert naive_mul(x, y) == x * y, f"Ошибка в naive_mul при x={x}, y={y}"
    print("3.4: naive_mul — все тесты пройдены!")

    # 3.5: fast_mul
    for _ in range(1000):
        x = random.randint(-1000, 1000)
        y = random.randint(0, 1000)
        assert fast_mul(x, y) == x * y, f"Ошибка в fast_mul при x={x}, y={y}"
    print("3.5: fast_mul — все тесты пройдены!")

    # 3.6: fast_pow
    for _ in range(1000):
        x = random.randint(-10, 10)
        y = random.randint(0, 20)
        assert fast_pow(x, y) == x ** y, f"Ошибка в fast_pow при x={x}, y={y}"
    print("3.6: fast_pow — все тесты пройдены!")

    # 3.7: mul16
    for _ in range(1000):
        x = random.randint(0, 0xFFFF)
        y = random.randint(0, 0xFFFF)
        assert mul16(x, y) == (x * y) & 0xFFFFFFFF, f"Ошибка в mul16 при x={x}, y={y}"
    print("3.7: mul16 — все тесты пройдены!")

    # 3.8: mul16k
    for _ in range(1000):
        x = random.randint(0, 0xFFFF)
        y = random.randint(0, 0xFFFF)
        assert mul16k(x, y) == (x * y) & 0xFFFFFFFF, f"Ошибка в mul16k при x={x}, y={y}"
    print("3.8: mul16k — все тесты пройдены!")

    # 3.9: fast_mul_gen
    print("\n3.9: примеры сгенерированного кода:")
    for y in [12, 15, 16, 7, 100, 0, 1]:
        code = fast_mul_gen(y)
        print(f"--- y = {y} ---")
        print(code)
        print()

        namespace = {}
        exec(code, namespace)
        f = namespace["f"]

        for _ in range(100):
            x = random.randint(-1000, 1000)
            assert f(x) == x * y, f"Ошибка в fast_mul_gen при x={x}, y={y}"
    print("3.9: fast_mul_gen — все тесты пройдены!")

    # 3.10: fast_pow_gen
    print("\n3.10: примеры сгенерированного кода:")
    for y in [5, 10, 0, 1, 13]:
        code = fast_pow_gen(y)
        print(f"--- y = {y} ---")
        print(code)
        print()

        namespace = {}
        exec(code, namespace)
        f = namespace["f"]

        for _ in range(50):
            x = random.randint(-10, 10)
            assert f(x) == x ** y, f"Ошибка в fast_pow_gen при x={x}, y={y}"
    print("3.10: fast_pow_gen — все тесты пройдены!")

    print("\nВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ УСПЕШНО!")
