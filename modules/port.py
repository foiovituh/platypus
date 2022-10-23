import socket

from modules.commons.messages import TIMEOUT_MUST_TO_BE_FLOAT
from modules.commons.utils import print_and_exit

ALL_PORTS = range(65536)
SUCCESS_RETURN_CODE = 0
COMMON_PORTS = (
    21, 22, 23, 25, 26, 53, 80, 110, 143,
    443,587, 993, 995, 2082, 2083, 3306, 8080,
)

def port_scan(target_host, timeout, sweep_all, verbose):
    print()
    try:
        timeout = float(timeout)
    except ValueError as value_error:
        print_and_exit(TIMEOUT_MUST_TO_BE_FLOAT, 1)
    for port in ALL_PORTS if sweep_all else COMMON_PORTS:
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client.settimeout(timeout)
        try:
            if tcp_client.connect_ex((target_host, port)) == SUCCESS_RETURN_CODE:
                _print_response("OPEN", target_host, port)
            elif verbose:
                _print_response("CLOSED", target_host, port)
        except Exception as exception:
            print_and_exit(exception.args[1], 1)

def _print_response(port_state, target_host, port):
    print("{} | {} => {}".format(port_state, target_host, port))
    