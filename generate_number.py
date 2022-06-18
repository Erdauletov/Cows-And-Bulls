def generate_number():

    import random

    def is_valid(num):
        num_set = set(num)
        return len(num_set) == len(num)

    number_range = input("""
=-_-=-_-=-_-=-= Cows & Bulls =-_-=-_-=-_-=-=
+-------------------------------------------+
|-- Выберите диапазон генерации числа:    --|
+-------------------------------------------+
|--     1  ->  (10, 100)                  --|
|--     2  ->  (100, 1000)                --|
|--     3  ->  (1000, 10000)              --|
+-------------------------------------------+
|--     >>  """)

    if number_range == ""   :
        print("""
+------------------------------------------+
|-- По умолчанию выбран диапазон << 2 >>  --|
+------------------------------------------+""")
        number_range = "2"

    range_dict = {'1': (10, 99),
                  '2': (100, 999),
                  '3': (1000, 9999)}

    hidden_number = str(random.randint(*range_dict[number_range]))

    while not is_valid(hidden_number):
        hidden_number = str(random.randint(*range_dict[number_range]))

    return hidden_number
