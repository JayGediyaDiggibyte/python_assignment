from src.list.util import process_list_commands
import pytest

def test_list_maintain(monkeypatch, capsys):
    inputs = iter([
        "12",
        "insert 0 5",
        "insert 1 10",
        "insert 0 6",
        "print",
        "remove 6",
        "append 9",
        "append 1",
        "sort",
        "print",
        "pop",
        "reverse",
        "print"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    process_list_commands()
    captured = capsys.readouterr()
    assert captured.out == (
        "[6, 5, 10]\n"
        "[1, 5, 9, 10]\n"
        "[9, 5, 1]\n"
    )
