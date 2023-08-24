"""
Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа
"""

summ_numbers = int(input('Введите сумму чисел : '))
product_numbers = int(input('Введите произведение чисел: '))
counting = summ_numbers ** 2 - 4 * product_numbers

if counting < 0:
    print("Не существует такой пары чисел")
else:
    a = (summ_numbers - (summ_numbers ** 2 - 4 * product_numbers) ** 0.5) / 2
    b = (summ_numbers + (summ_numbers ** 2 - 4 * product_numbers) ** 0.5) / 2
    if a > 1000 or b > 1000:
        print("Числа должны быть меньше 1000")
    else:
        x = a - int(a)
        y = b - int(b)
        if x == 0 and y == 0:
            print(f"Петя назвал сумму чисел - {summ_numbers} и произведение чисел - {product_numbers}")
            print(f"Петя задумывал натуральные числа - {int(a), int(b)}")
        else:
            print("Не удалось определить пару чисел")
