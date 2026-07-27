from pytest import raises

from platypus.commons.utils import print_and_exit


def test_print_and_exit(capsys):
    with raises(SystemExit) as exception:
        print_and_exit("error message", 1)

    captured = capsys.readouterr()

    assert captured.out == "error message\n"
    assert exception.value.code == 1
