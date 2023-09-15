import os
from colorama import init, Fore, Style

def clear_cmd():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_large_text(text):
    init(autoreset=True)
    print(Fore.YELLOW + Style.BRIGHT + text)
    print(Style.RESET_ALL)

def main():
    clear_cmd()
    print_large_text("------------------------------------------------------------------")
    print_large_text("\n                        CAP TOOLS                       \n")
    print_large_text("------------------------------------------------------------------")

if __name__ == "__main__":
    main()