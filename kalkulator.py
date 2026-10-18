import os

from colorama import Fore, Style


class Calculator:
    def __init__(self) -> None:
        self.allowed_operations = ["+", "-", "*", "/", "^", "root"]

    def _ask_for_number(self, number_index: int = 0) -> float:
        while True:
            try:
                return float(
                    input(f"{Fore.CYAN}Enter number {number_index}> {Style.RESET_ALL}")
                )
            except ValueError:
                print(f"{Fore.RED}Must be a valid number.{Style.RESET_ALL}")

    def get_numbers(self) -> tuple:
        number1 = self._ask_for_number(number_index=1)
        number2 = self._ask_for_number(number_index=2)
        return number1, number2

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def get_operation(self) -> str:
        while True:
            op = input(
                f"{Fore.CYAN}Enter operation ({', '.join(self.allowed_operations)})> {Style.RESET_ALL}"
            ).strip()

            if op in self.allowed_operations:
                return op

            print(
                f"{Fore.RED}Invalid operation. Choose from: {', '.join(self.allowed_operations)}{Style.RESET_ALL}"
            )

    def format_number(self, value: float) -> int | float:
        if value.is_integer():
            return int(value)
        return value

    def start_calculator(self) -> None:
        while True:
            self.clear()
            print(f"{Fore.YELLOW}=== Calculator ==={Style.RESET_ALL}")

            num1, num2 = self.get_numbers()

            op = self.get_operation()

            match op:
                case "+":
                    result = num1 + num2

                case "-":
                    result = num1 - num2

                case "*":
                    result = num1 * num2

                case "/":
                    result = (
                        num1 / num2
                        if num2 != 0
                        else f"{Fore.RED}Error (Division by zero){Style.RESET_ALL}"
                    )

                case "^":
                    result = num1**num2

                case "root":
                    result = (
                        num1 ** (1 / num2)
                        if num2 != 0
                        else f"{Fore.RED}Error (Zero root index){Style.RESET_ALL}"
                    )

                case _:
                    result = f"{Fore.RED}Error{Style.RESET_ALL}"

            f_num1 = self.format_number(num1)
            f_num2 = self.format_number(num2)
            f_result = (
                self.format_number(result) if isinstance(result, float) else result
            )

            print(
                f"\n{Fore.GREEN}Result: {f_num1} {op} {f_num2} = {f_result}{Style.RESET_ALL}"
            )

            choice = (
                input(
                    f"\n{Fore.MAGENTA}Do you want to do another calculation? (y/n): {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
            if choice != "y":
                print(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
                break


def main():
    Calculator().start_calculator()


if __name__ == "__main__":
    main()
