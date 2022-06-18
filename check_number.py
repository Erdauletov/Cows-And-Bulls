def check_number(hidden_number, guessed_number):

    cows = 0
    bulls = 0

    for i in range(len(hidden_number)):
        bulls += 1 if hidden_number[i] == guessed_number[i] else 0
        cows += 1 if hidden_number[i] in guessed_number and hidden_number[i] != guessed_number[i] else 0

    return cows, bulls
