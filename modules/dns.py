import dns.resolver
from modules.commons.messages import (
    ALL_NAME_SERVERS_FAILED,
    CHECK_YOUR_INTERNET_CONNECTION,
    DNS_QUERY_NAME_NOT_EXISTS,
    NOT_FOUND,
)
from modules.commons.utils import print_and_exit

DNS_RECORD_TYPE = "A"
OK_STATUS_CODE = "200"
NOT_FOUND_STATUS_CODE = "404"
RESOLVER = dns.resolver.Resolver()

def execute_subdomain_bruteforce(target_host, word_list_path):
    print()
    word_list_lines = _get_word_list_lines(word_list_path)
    for subdomain_to_test in word_list_lines:
        subdomain = "{}.{}".format(subdomain_to_test, target_host)
        try:
            ip_addresses = RESOLVER.resolve(subdomain, DNS_RECORD_TYPE)
            for ip_address in ip_addresses:
                _print_response(subdomain, ip_address)
        except Exception as error:
            error_message = error.__class__().args[0]
            if error_message == DNS_QUERY_NAME_NOT_EXISTS:
                _print_response(subdomain, NOT_FOUND, NOT_FOUND_STATUS_CODE)
            elif error_message == ALL_NAME_SERVERS_FAILED:
                print_and_exit(CHECK_YOUR_INTERNET_CONNECTION, 1)

def _print_response(subdomain, ip_address, status_code = OK_STATUS_CODE):
    print("{} | {} => {}".format(status_code, subdomain, ip_address))

def _get_word_list_lines(word_list_path):
    try:
        with open(word_list_path, "r") as word_list:
            return word_list.read().splitlines()
    except FileNotFoundError as error:
        print_and_exit(error.args[1] + ": " + word_list_path, 1)
