ALL_NAME_SERVERS_FAILED = "All nameservers failed to answer the query."
CHECK_YOUR_INTERNET_CONNECTION = "Check your internet connection"
DNS_QUERY_NAME_NOT_EXISTS = "The DNS query name does not exist."
HELP = "USAGE: python3 platypus.py [module type] [optional flags...]\n" \
    "MODULES:\n" \
    "  --sb (DNS subdomain bruteforce)\n" \
    "  --ps (Port scan) [--all, 65536 ports, optional]" \
    "  [--v, verbose, optional]\n" \
    "    DEFAULT_PORTS_TO_BE_SCANNED:\n" \
    "      21, 22, 23, 25, 26, 53, 80, 110, 143,\n" \
    "      443, 587, 993, 995, 2082, 2083, 3306, 8080\n" \
    "EXAMPLES:\n" \
    "  python3 platypus.py --sb\n" \
    "  host name: google.com\n" \
    "  word list path: word_lists/example-10.txt\n\n" \
    "  python3 platypus.py --ps --a\n" \
    "  host name: bancocn.com\n" \
    "  timeout: 0.05\n" \
    "FOR MORE INFORMATION, SEE: https://github.com/foiovituh/platypus"
INVALID_ARGUMENTS = "Invalid arguments! Use --h flag for help"
NOT_FOUND = "NOT_FOUND"
MISSING_ARGUMENTS = "Missing arguments! Use --h flag for help"
TIMEOUT_MUST_TO_BE_FLOAT = "Timeout must to be float value, example: 0.05"
