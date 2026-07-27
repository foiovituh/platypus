from unittest.mock import mock_open, patch

import pytest
from dns.exception import Timeout
from dns.resolver import NXDOMAIN, NoNameservers

from platypus.commons.constants import NOT_FOUND_RESPONSE
from platypus.dns import (
    _get_word_list_lines,
    execute_subdomain_bruteforce,
)


def test_get_word_list_lines_success():
    fake_content = "www\napi\nadmin"

    with patch(
        "builtins.open",
        mock_open(read_data=fake_content),
    ):
        result = _get_word_list_lines("wordlist.txt")

    assert result == [
        "www",
        "api",
        "admin",
    ]


def test_get_word_list_lines_file_not_found():
    with (
        patch(
            "builtins.open",
            side_effect=FileNotFoundError,
        ),
        pytest.raises(SystemExit) as exception,
    ):
        _get_word_list_lines("missing.txt")

    assert exception.value.code == 1


def test_execute_subdomain_bruteforce_found(capsys):
    resolver_response = [
        "192.0.2.10",
    ]

    with (
        patch(
            "platypus.dns._get_word_list_lines",
            return_value=["www"],
        ),
        patch(
            "platypus.dns.DNS_RESOLVER.resolve",
            return_value=resolver_response,
        ),
    ):
        execute_subdomain_bruteforce(
            "example.com",
            "wordlist.txt",
        )

    captured = capsys.readouterr()

    assert "200 | www.example.com => 192.0.2.10" in captured.out


def test_execute_subdomain_bruteforce_not_found(capsys):
    with (
        patch(
            "platypus.dns._get_word_list_lines",
            return_value=["admin"],
        ),
        patch(
            "platypus.dns.DNS_RESOLVER.resolve",
            side_effect=NXDOMAIN,
        ),
    ):
        execute_subdomain_bruteforce(
            "example.com",
            "wordlist.txt",
        )

    captured = capsys.readouterr()

    assert f"404 | admin.example.com => {NOT_FOUND_RESPONSE}" in captured.out


def test_execute_subdomain_bruteforce_no_nameservers():
    with (
        patch(
            "platypus.dns._get_word_list_lines",
            return_value=["www"],
        ),
        patch(
            "platypus.dns.DNS_RESOLVER.resolve",
            side_effect=NoNameservers,
        ),
        pytest.raises(SystemExit),
    ):
        execute_subdomain_bruteforce(
            "example.com",
            "wordlist.txt",
        )


def test_execute_subdomain_bruteforce_timeout(capsys):
    with (
        patch(
            "platypus.dns._get_word_list_lines",
            return_value=["www"],
        ),
        patch(
            "platypus.dns.DNS_RESOLVER.resolve",
            side_effect=Timeout,
        ),
    ):
        execute_subdomain_bruteforce(
            "example.com",
            "wordlist.txt",
        )

    captured = capsys.readouterr()

    assert "408 | www.example.com => TIMEOUT" in captured.out
