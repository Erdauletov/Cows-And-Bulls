def input_number(hidden_number):
    def is_valid(num):
        num_set = set(num)
        is_digit = num.isdigit()
        is_valid_len = len(num) == len(hidden_number)

        try:
            is_valid_num = len(num_set) == len(num) and (num[0] != '0')
            return is_valid_len and is_digit and is_valid_num
        except IndexError:
            return False

    guessed_number = input("""
+------------------------------------------+
|-- Введите число в выбранном диапазоне: --|
+------------------------------------------+
|--     >>  """)

    while not is_valid(guessed_number):
        guessed_number = input("""
+------------------------------------------+
|-- Вы ввели неправильное число!         --|
|-- Введите число в выбранном диапазоне: --|
+------------------------------------------+
|--     >>  """)

    return guessed_number
