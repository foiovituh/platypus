import argparse

from . import dns
from . import email
from . import port


def main() -> None:
    parser = _create_parser()
    args = parser.parse_args()

    if not hasattr(args, "function"):
        parser.print_help()

        return

    args.function(args)


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="security enumeration tool.")

    subparsers = parser.add_subparsers(metavar="COMMAND")

    _add_dns_parser(subparsers)
    _add_port_parser(subparsers)
    _add_email_parser(subparsers)

    return parser


def _add_dns_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "subdomains",
        help="DNS subdomain bruteforce",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show all results, including non-existent subdomains",
    )
    parser.add_argument("host")
    parser.add_argument("wordlist")
    parser.set_defaults(function=_execute_sudomains)


def _add_port_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "ports",
        help="TCP port scan",
    )
    parser.add_argument("host")
    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=0.5,
        metavar="SECONDS",
        help="Timeout in seconds (default: 0.5)",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Scan all TCP ports",
    )
    parser.add_argument(
        "-p",
        "--ports",
        metavar="PORTS",
        help="Scan specific ports (e.g. 22,80,443)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show closed ports",
    )
    parser.set_defaults(function=_execute_ports)


def _add_email_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "emails",
        help="HTML email finder",
    )
    parser.add_argument("target")
    parser.set_defaults(function=_execute_emails)


def _execute_sudomains(args: argparse.Namespace) -> None:
    dns.execute_subdomain_bruteforce(
        args.verbose,
        args.host,
        args.wordlist,
    )


def _execute_ports(args: argparse.Namespace) -> None:
    port.execute_port_scan(
        args.host,
        args.timeout,
        args.all,
        args.verbose,
        args.ports,
    )


def _execute_emails(args: argparse.Namespace) -> None:
    email.execute_email_finder(args.target)


if __name__ == "__main__":
    main()
