import sys


def print_and_exit(message: str, exit_code: int) -> None:
    print(message)

    sys.exit(exit_code)
