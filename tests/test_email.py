import httpx

from platypus import email


def test_email_finder_finds_email(monkeypatch: str, capsys: str):
    response = httpx.Response(
        200,
        text="Contact financeiro@example.com",
    )

    monkeypatch.setattr(httpx, "get", lambda *args, **kwargs: response)

    email.execute_email_finder("example.com")

    assert "financeiro@example.com" in capsys.readouterr().out


def test_email_finder_reports_no_email(monkeypatch: str, capsys: str):
    response = httpx.Response(
        200,
        text="No email here",
    )

    monkeypatch.setattr(httpx, "get", lambda *args, **kwargs: response)

    email.execute_email_finder("example.com")

    assert "NO_EMAIL_FOUND:" in capsys.readouterr().out


def test_email_finder_reports_connection_refused(monkeypatch: str, capsys: str):
    request = httpx.Request("GET", "http://example.com")
    error = httpx.ConnectError(
        "Connection refused",
        request=request,
    )

    monkeypatch.setattr(
        httpx, "get", lambda *args, **kwargs: (_ for _ in ()).throw(error)
    )

    email.execute_email_finder("example.com")

    assert "CONNECTION_FAILED:" in capsys.readouterr().out
