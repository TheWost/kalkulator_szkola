import os
from colorama import Fore, Style


def invalid_input(prompt="Invalid input"):
    input(Fore.RED + prompt + Style.RESET_ALL)

def get_user_number() -> float:
    while True:
        try:
            liczba = float(input(Fore.YELLOW + "Enter number: " + Style.RESET_ALL))
            print(Fore.GREEN + Style.BRIGHT + "Good number!" + Style.RESET_ALL)

            return liczba
        except ValueError:
            os.system("cls")
            invalid_input()

def calculate(number1, number2):
    while True:

        os.system("cls")
        print("""
1. Dodawanie
2.Odejmowanie
3.dzielenie
4.mnozenie
5.Potegowanie
6.pierwiastkowanie
""")

        user_choice = input(Fore.YELLOW + Style.BRIGHT + "> " + Style.RESET_ALL)

        match user_choice:
            case "1":
                return number1 + number1

            case "2":
                return number1 - number2

            case "3":
                return number1 / number2

            case "4":
                return number1 * number2

            case "5":
                return number1 ** number2

            case "6":
                return number1 ** (1 / number2)

            case _:
                invalid_input()



def main():
    os.system("cls")
    number1 = get_user_number()
    number2 = get_user_number()

    number = calculate(number1, number2)

    if number.is_integer():
        print(int(number))
    else:
        print(number)


if __name__ == "__main__":
    main()
