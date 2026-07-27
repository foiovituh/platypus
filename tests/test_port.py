from unittest.mock import MagicMock, patch

import pytest

from platypus.port import execute_port_scan


def test_execute_port_scan_open_port(capsys):
    socket_mock = MagicMock()

    socket_mock.__enter__.return_value.connect_ex.return_value = 0

    with (
        patch(
            "platypus.port.socket.socket",
            return_value=socket_mock,
        ),
        patch(
            "platypus.port.COMMON_PORTS",
            [80],
        ),
    ):
        execute_port_scan(
            "localhost",
            "0.5",
            False,
            False,
        )

    captured = capsys.readouterr()

    assert "OPEN | localhost => 80" in captured.out


def test_execute_port_scan_closed_port_verbose(capsys):
    socket_mock = MagicMock()

    socket_mock.connect_ex.return_value = 1

    with (
        patch(
            "platypus.port.socket.socket",
            return_value=socket_mock,
        ),
        patch(
            "platypus.port.COMMON_PORTS",
            [80],
        ),
    ):
        execute_port_scan(
            "localhost",
            "0.5",
            False,
            True,
        )

    captured = capsys.readouterr()

    assert "CLOSED | localhost => 80" in captured.out


def test_execute_port_scan_invalid_timeout():
    with pytest.raises(SystemExit) as exception:
        execute_port_scan(
            "localhost",
            "abc",
            False,
            False,
        )

    assert exception.value.code == 1


def test_execute_port_scan_socket_error():
    socket_mock = MagicMock()

    socket_mock.__enter__.return_value.connect_ex.side_effect = OSError(
        "connection error"
    )

    with (
        patch(
            "platypus.port.socket.socket",
            return_value=socket_mock,
        ),
        patch(
            "platypus.port.COMMON_PORTS",
            [80],
        ),
        pytest.raises(SystemExit),
    ):
        execute_port_scan(
            "localhost",
            "0.5",
            False,
            False,
        )
