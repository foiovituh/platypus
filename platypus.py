from modules.commons.messages import (
    HELP,
    INVALID_ARGUMENTS,
    MISSING_ARGUMENTS
)
from modules.commons.utils import print_and_exit
from modules.dns import execute_subdomain_bruteforce
from pyfiglet import print_figlet
from sys import argv

def main():
    if len(argv) == 1:
        print_and_exit(MISSING_ARGUMENTS, 1)
    elif argv[1] == "--h":
        print_and_exit(HELP, 0)
    elif argv[1] == "--sb":
        execute_subdomain_bruteforce(
            input("host name: "),
            input("word list path: "),
        )
    else:
        print_and_exit(INVALID_ARGUMENTS, 1)

if __name__ == "__main__":
    print_figlet("platypus", "standard")
    main()
