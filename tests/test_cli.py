from unittest.mock import patch

from platypus.cli import main


def test_cli_subdomain_bruteforce():
    with (
        patch(
            "sys.argv",
            [
                "platypus",
                "--sb",
                "example.com",
                "word_lists/tiny-10.txt",
            ],
        ),
        patch(
            "platypus.cli.print_figlet",
        ),
        patch(
            "platypus.cli.execute_subdomain_bruteforce",
        ) as execute_subdomain_bruteforce,
    ):
        main()

    execute_subdomain_bruteforce.assert_called_once_with(
        "example.com",
        "word_lists/tiny-10.txt",
    )


def test_cli_port_scan():
    with (
        patch(
            "sys.argv",
            [
                "platypus",
                "--ps",
                "127.0.0.1",
            ],
        ),
        patch(
            "platypus.cli.print_figlet",
        ),
        patch(
            "platypus.cli.execute_port_scan",
        ) as execute_port_scan,
    ):
        main()

    execute_port_scan.assert_called_once_with(
        "127.0.0.1",
        0.5,
        False,
        False,
    )


def test_cli_without_arguments(capsys):
    with patch(
        "sys.argv",
        [
            "platypus",
        ],
    ):
        main()

    captured = capsys.readouterr()

    assert "usage:" in captured.out
    assert "--sb" in captured.out
    assert "--ps" in captured.out
