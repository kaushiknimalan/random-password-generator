#import converter
import needed_value_generator
import random

password = ["", "", "", "", "", "", "", ""]


def generate_and_return_password():
    needed_value_generator.value_generator()

    i = 1
    j = 1
    k = 1
    l = 1

    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0


    while i <= 2:
        uppercase_letters = needed_value_generator.upper_letters[i-1]
        number1 = random.randint(0, 7)

        if number1 == number2:
            continue
        elif number1 == number3:
            continue
        elif number1 == number4:
            continue


        password.insert(number3, uppercase_letters)
        i += 1

    while j <= 2:
        number2 = random.randint(0, 7)
        lower_letters = needed_value_generator.lowercase_letters[j-1]

        if number2 == number1:
            continue
        elif number2 == number3:
            continue
        elif number2 == number4:
            continue


        password.insert(number3, lower_letters)
        j += 1

    while k <= 2:
        number3 = random.randint(0, 7)
        numbers = needed_value_generator.numbers[k-1]

        if number3 == number1:
            continue
        elif number3 == number2:
            continue
        elif number3 == number4:
            continue


        password.insert(number3, numbers)
        k += 1

    while l <= 2:
        number4 = random.randint(0, 7)
        punctuation = needed_value_generator.punctuation_signs[l-1]

        if number4 == number1:
            continue
        elif number4 == number2:
            continue
        elif number4 == number3:
            continue



        password.insert(number3, punctuation)
        l += 1

        i = 1
        list_value = ""
        converted_value = ""
        while i <= len(password):
            list_value = password[i - 1]
            print(list_value)
            if list_value == " ":
                password.remove(list_value)
            else:
                converted_value += list_value
            i += 1
    print(converted_value)


