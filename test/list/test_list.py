from src.list.util import process_list_commands
import pytest

@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (
            [
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
            ],
            (
                "[6, 5, 10]\n"
                "[1, 5, 9, 10]\n"
                "[9, 5, 1]\n"
            )
        ),
        (
            [
                "8",
                "append 3",
                "append 2",
                "append 1",
                "print",
                "sort",
                "print",
                "reverse",
                "print"
            ],
            (
                "[3, 2, 1]\n"
                "[1, 2, 3]\n"
                "[3, 2, 1]\n"
            )
        )
    ]
)

def test_process_list_commands(monkeypatch, capsys, inputs, expected_output):
    input_iter = iter(inputs)
    monkeypatch.setattr(
        "builtins.input",
        lambda: next(input_iter)
    )

    process_list_commands()
    captured = capsys.readouterr()
    assert captured.out == expected_output
