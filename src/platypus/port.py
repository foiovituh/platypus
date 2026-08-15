import socket

from .utils import print_and_exit


ALL = range(1, 65536)
COMMON = (
    21,  # FTP
    22,  # SSH
    23,  # Telnet
    25,  # SMTP
    53,  # DNS
    80,  # HTTP
    110,  # POP3
    111,  # RPCbind
    135,  # MS RPC
    139,  # NetBIOS
    143,  # IMAP
    443,  # HTTPS
    445,  # SMB
    554,  # RTSP
    587,  # SMTP submission
    993,  # IMAPS
    995,  # POP3S
    1025,  # Microsoft RPC / dynamic service
    1433,  # Microsoft SQL Server
    1521,  # Oracle Database
    1723,  # PPTP
    3306,  # MySQL
    3389,  # RDP
    5432,  # PostgreSQL
    5900,  # VNC
    8080,  # HTTP alternate
    8443,  # HTTPS alternate
    8888,  # HTTP alternate
)


def execute_port_scan(
    target: str,
    timeout: float = 0.5,
    sweep_all: bool = False,
    verbose: bool = True,
    ports: str | None = None,
) -> None:
    if ports:
        try:
            to_scan = [int(port) for port in ports.split(",")]
        except ValueError:
            print_and_exit(f"INVALID_PORTS: {ports}", 1)
    elif sweep_all:
        to_scan = ALL
    else:
        to_scan = COMMON

    for port in to_scan:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
            tcp_client.settimeout(timeout)

            try:
                result = tcp_client.connect_ex((target, port))
            except OSError as error:
                print_and_exit(str(error), 1)

            status = "OPEN" if result == 0 else "CLOSED"

            if not verbose and status == "CLOSED":
                continue

            print(f"{status}: {port}")
