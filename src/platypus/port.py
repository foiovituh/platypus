import socket

from platypus.commons.messages import TIMEOUT_MUST_BE_A_FLOAT
from platypus.commons.utils import print_and_exit

ALL_PORTS = range(65536)
COMMON_PORTS = (
    21,
    22,
    23,
    25,
    26,
    53,
    80,
    110,
    143,
    443,
    587,
    993,
    995,
    2082,
    2083,
    3306,
    8080,
)
SUCCESS_RETURN_CODE = 0


def execute_port_scan(
    target_host: str,
    timeout: float,
    sweep_all: bool,
    verbose: bool,
) -> None:
    print()

    try:
        timeout = float(timeout)
    except ValueError:
        print_and_exit(TIMEOUT_MUST_BE_A_FLOAT, 1)

    ports = ALL_PORTS if sweep_all else COMMON_PORTS

    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
            tcp_client.settimeout(timeout)

            try:
                if tcp_client.connect_ex((target_host, port)) == SUCCESS_RETURN_CODE:
                    _print_response("OPEN", target_host, port)
                elif verbose:
                    _print_response("CLOSED", target_host, port)
            except OSError as error:
                print_and_exit(str(error), 1)


def _print_response(port_state: str, target_host: str, port: int) -> None:
    print(f"{port_state} | {target_host} => {port}")
