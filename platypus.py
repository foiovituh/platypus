from modules.commons.messages import (
    HELP,
    INVALID_ARGUMENTS,
    MISSING_ARGUMENTS
)
from modules.commons.utils import print_and_exit
from modules.dns import execute_subdomain_bruteforce
from modules.port import port_scan
from pyfiglet import print_figlet
from sys import argv

SELECTOR = ""
TOOLS = {
    "subdomain_bruteforce":"--sb",
    "port_scan":"--ps",
}

def _main():

    try:
        SELECTOR = argv[1]
    except IndexError as index_error:
        print_and_exit(MISSING_ARGUMENTS, 1)
    if SELECTOR == "--h":
        print_and_exit(HELP, 0)
    elif SELECTOR not in TOOLS.values():
        print_and_exit(INVALID_ARGUMENTS, 1)
    elif SELECTOR == TOOLS["subdomain_bruteforce"]:
        execute_subdomain_bruteforce(
            _get_host_name,
            input("word list path: "),
        )
    elif SELECTOR == TOOLS["port_scan"]:
        port_scan(
            _get_host_name(),
            input("timeout: "),
            argv.__contains__("--all"),
            argv.__contains__("--v"),
        )


def _get_host_name():
    return input("host name: ")

if __name__ == "__main__":
    print_figlet("platypus", "standard")
    _main()
