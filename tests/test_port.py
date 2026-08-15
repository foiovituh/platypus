import pytest

from platypus import port


def test_port_scan_uses_common_ports(monkeypatch: str, capsys: str):
    scanned = []

    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def settimeout(self, timeout):
            pass

        def connect_ex(self, address):
            scanned.append(address[1])
            return 0

    monkeypatch.setattr(port.socket, "socket", lambda *args: FakeSocket())

    port.execute_port_scan("localhost")

    assert scanned == list(port.COMMON)
    assert "OPEN: 21" in capsys.readouterr().out


def test_port_scan_uses_custom_ports(monkeypatch: str):
    scanned = []

    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def settimeout(self, timeout):
            pass

        def connect_ex(self, address):
            scanned.append(address[1])
            return 0

    monkeypatch.setattr(port.socket, "socket", lambda *args: FakeSocket())

    port.execute_port_scan("localhost", ports="2,3,7")

    assert scanned == [2, 3, 7]


def test_port_scan_rejects_invalid_ports():
    with pytest.raises(SystemExit) as error:
        port.execute_port_scan("localhost", ports="2,x,7")

    assert error.value.code == 1
