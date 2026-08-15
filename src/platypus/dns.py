import dns.exception
import dns.resolver

from . import utils


def execute_subdomain_bruteforce(
    verbose: bool,
    target: str,
    word_list_path: str,
) -> None:
    resolver = dns.resolver.Resolver()

    try:
        resolver.resolve(target, "A")
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        utils.print_and_exit(f"INVALID_TARGET: {target}", 1)
    except dns.resolver.NoNameservers:
        utils.print_and_exit(f"NO_DNS_SERVERS_RESPONDED: {target}", 1)
    except dns.exception.Timeout:
        utils.print_and_exit(f"TIMEOUT: {target}", 1)

    found = False

    for line in _get_word_list_lines(word_list_path):
        subdomain = f"{line}.{target}"
        status = ""

        try:
            answers = resolver.resolve(subdomain, "A")
            ips = ", ".join([str(ip) for ip in answers])
            status = f"OK: {subdomain} ({ips})"
            found = True
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            status = f"NOT_FOUND: {subdomain}"
        except dns.resolver.NoNameservers:
            status = f"NO_DNS_SERVERS_RESPONDED: {subdomain}"
        except dns.exception.Timeout:
            status = f"TIMEOUT: {subdomain}"

        if not verbose and not status.startswith("OK:"):
            continue

        print(status)

    if not found:
        print(f"NO_SUBDOMAIN_FOUND: {target}")


def _get_word_list_lines(path: str) -> list[str]:
    try:
        with open(path) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        utils.print_and_exit(f"FILE_NOT_FOUND: {path}", 1)
