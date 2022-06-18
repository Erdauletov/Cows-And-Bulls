from generate_number import generate_number
from check_number import check_number
from input_number import input_number
import os


def game():
    hidden_number = generate_number()
    guessed_number = input_number(hidden_number)
    guess_counter = 0

    cows, bulls = check_number(hidden_number, guessed_number)

    while True:
        print()
        print(f"""+------------------------------------------+
|-- число - {guessed_number} | коров - {cows} | быков - {bulls} --|
+------------------------------------------+""")
        guess_counter += 1
        if bulls != len(hidden_number):
            guessed_number = input_number(hidden_number)
            cows, bulls = check_number(hidden_number, guessed_number)
        else:
            print(f"""
+------------------------------------------+
|-- Вы угадали!                          --|
|-- Количество попыток: {guess_counter}                --|
+------------------------------------------+
""")
            break

    again = input("""+------------------------------------------+
|--  Хотите еще? (да \ нет)              --|
+------------------------------------------+
|--     >>  """)

    return {"да": True, "lf": True}.get(again, False)


while True:
    os.system('cls')
    flag = game()
    if flag is False:
        print("Спасибо за игру!")
        break
