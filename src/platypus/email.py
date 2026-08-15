import httpx
import re
import ssl


def execute_email_finder(
    target: str, timeut: float = 5, follow_redirects: bool = True
) -> None:
    http_prefix = "http://"
    https_prefix = "https://"
    pattern = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
    status = {
        403: "FORBIDDEN",
        406: "NOT_ACCEPTABLE",
        429: "RATE_LIMIT",
    }

    if target.startswith((http_prefix, https_prefix)):
        urls = [target]
    else:
        urls = [f"{http_prefix}{target}", f"{https_prefix}{target}"]

    emails = []

    for url in urls:
        try:
            response = httpx.get(url, timeout=timeut, follow_redirects=follow_redirects)

            if response.status_code in (status.keys()):
                print(f"{status[response.status_code]}: {url}")

                continue

            emails = pattern.findall(response.text)

            if not emails:
                print(f"NO_EMAIL_FOUND: {url}")

                continue

            emails.sort()

            for email in emails:
                print(email)
        except httpx.ConnectError as error:
            print(f"{_get_connection_status(error)}: {url}")

            continue


def _is_ssl_error(error: Exception) -> bool:
    while error:
        if isinstance(error, ssl.SSLError):
            return True

        error = error.__cause__ or error.__context__

    return False


def _get_connection_status(error: httpx.RequestError) -> str:
    if isinstance(error, httpx.ConnectTimeout):
        return "CONNECTION_TIMEOUT"

    if isinstance(error, httpx.ConnectError):
        cause = error.__cause__

        if isinstance(cause, ConnectionRefusedError):
            return "CONNECTION_REFUSED"

        if _is_ssl_error(error):
            return "SSL_CONNECTION_FAILED"

        return "CONNECTION_FAILED"

    return "REQUEST_FAILED"
