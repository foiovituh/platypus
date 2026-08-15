from unittest.mock import Mock

import dns.resolver

from platypus import dns as platypus_dns


def test_subdomain_bruteforce_finds_subdomain(
    monkeypatch: str, tmp_path: str, capsys: str
):
    wordlist = tmp_path / "words.txt"
    wordlist.write_text("www\n")

    resolver = Mock()
    resolver.resolve.side_effect = [
        [Mock()],
        [Mock(__str__=lambda self: "1.2.3.4")],
    ]

    monkeypatch.setattr(
        platypus_dns.dns.resolver,
        "Resolver",
        lambda: resolver,
    )

    platypus_dns.execute_subdomain_bruteforce(
        False,
        "example.com",
        str(wordlist),
    )

    assert "OK: www.example.com (1.2.3.4)" in capsys.readouterr().out


def test_subdomain_bruteforce_reports_no_results(
    monkeypatch: str, tmp_path: str, capsys: str
):
    wordlist = tmp_path / "words.txt"
    wordlist.write_text("www\n")

    resolver = Mock()
    resolver.resolve.side_effect = [
        [Mock()],
        dns.resolver.NXDOMAIN(),
    ]

    monkeypatch.setattr(
        platypus_dns.dns.resolver,
        "Resolver",
        lambda: resolver,
    )

    platypus_dns.execute_subdomain_bruteforce(
        False,
        "example.com",
        str(wordlist),
    )

    assert "NO_SUBDOMAIN_FOUND: example.com" in capsys.readouterr().out


def test_subdomain_bruteforce_rejects_invalid_target(monkeypatch: str, tmp_path: str):
    wordlist = tmp_path / "words.txt"
    wordlist.write_text("www\n")

    resolver = Mock()
    resolver.resolve.side_effect = dns.resolver.NXDOMAIN()

    monkeypatch.setattr(
        platypus_dns.dns.resolver,
        "Resolver",
        lambda: resolver,
    )

    try:
        platypus_dns.execute_subdomain_bruteforce(
            False,
            "invalid.test",
            str(wordlist),
        )
    except SystemExit as error:
        assert error.code == 1
