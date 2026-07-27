from argparse import ArgumentParser, RawTextHelpFormatter

from pyfiglet import print_figlet

from platypus.dns import execute_subdomain_bruteforce
from platypus.port import execute_port_scan


def main():
    parser = ArgumentParser(
        description="Platypus - Generic information gathering scanner",
        formatter_class=RawTextHelpFormatter,
    )

    parser.add_argument(
        "--sb",
        nargs=2,
        metavar=("HOST", "WORDLIST"),
        help="DNS subdomain bruteforce",
    )

    parser.add_argument(
        "--ps",
        metavar="HOST",
        help="TCP port scan",
    )

    args = parser.parse_args()

    if args.sb:
        print_figlet("platypus", "standard")

        host, wordlist = args.sb

        execute_subdomain_bruteforce(
            host,
            wordlist,
        )

        return

    if args.ps:
        print_figlet("platypus", "standard")

        execute_port_scan(
            args.ps,
            0.5,
            False,
            False,
        )

        return

    parser.print_help()


if __name__ == "__main__":
    main()
