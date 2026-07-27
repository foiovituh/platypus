import dns.exception
import dns.resolver

from platypus.commons.constants import (
    DNS_RECORD_TYPE,
    NOT_FOUND_RESPONSE,
    NOT_FOUND_STATUS_CODE,
    OK_STATUS_CODE,
    TIMEOUT_RESPONSE,
    TIMEOUT_STATUS_CODE,
)
from platypus.commons.messages import (
    DNS_NO_NAMESERVERS,
    FILE_NOT_FOUND,
)
from platypus.commons.utils import print_and_exit

DNS_RESOLVER = dns.resolver.Resolver()


def execute_subdomain_bruteforce(
    target_host_or_ipv4: str,
    word_list_path: str,
) -> None:
    print()

    for subdomain_to_test in _get_word_list_lines(word_list_path):
        subdomain = f"{subdomain_to_test}.{target_host_or_ipv4}"

        try:
            ip_addresses = DNS_RESOLVER.resolve(
                subdomain,
                DNS_RECORD_TYPE,
            )

            for ip_address in ip_addresses:
                _print_response(
                    subdomain,
                    ip_address,
                )
        except dns.resolver.NXDOMAIN:
            _print_response(
                subdomain,
                NOT_FOUND_RESPONSE,
                NOT_FOUND_STATUS_CODE,
            )
        except dns.resolver.NoAnswer:
            _print_response(
                subdomain,
                NOT_FOUND_RESPONSE,
                NOT_FOUND_STATUS_CODE,
            )
        except dns.resolver.NoNameservers:
            print_and_exit(
                DNS_NO_NAMESERVERS,
                1,
            )
        except dns.exception.Timeout:
            _print_response(
                subdomain,
                TIMEOUT_RESPONSE,
                TIMEOUT_STATUS_CODE,
            )


def _get_word_list_lines(word_list_path: str) -> list[str]:
    try:
        with open(word_list_path, "r") as word_list:
            return word_list.read().splitlines()

    except FileNotFoundError:
        print_and_exit(
            f"{FILE_NOT_FOUND}: {word_list_path}",
            1,
        )


def _print_response(
    subdomain: str,
    ip_address,
    status_code: str = OK_STATUS_CODE,
) -> None:
    print(f"{status_code} | {subdomain} => {ip_address}")
