import random
import Numerical_Alphabets_values

uppercase_letters = []
lowercase_letters = []
numbers = []
punctuation_signs = []
upper_letters = uppercase_letters


def value_generator():
    i = 1
    j = 1
    k = 1
    l = 1

    while i <= 2:
        random_number = random.randint(1, 26)
        upper_letters.append(Numerical_Alphabets_values.higher_alpha_numerical_values[random_number])
        i += 1

    while j <= 2:
        random_number = random.randint(1, 26)
        lowercase_letters.append(Numerical_Alphabets_values.lower_alpha_numerical_values[random_number])
        j += 1

    while k <= 2:
        random_number_fpunctuation = random.randint(1, 14)
        punctuation_signs.append(Numerical_Alphabets_values.punctuation_signs[random_number_fpunctuation])
        k += 1

    while l <= 2:
        random_number_fnumber = random.randint(1, 50)
        random_number_fnumber = str(random_number_fnumber)
        numbers.append(random_number_fnumber)
        l += 1
