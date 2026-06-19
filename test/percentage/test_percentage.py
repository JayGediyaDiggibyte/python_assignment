from src.percentage.util import finding_percentage
import pytest

@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            [
                "3",
                "Krishna 67 68 69",
                "Arjun 70 98 63",
                "Malika 52 56 60",
                "Malika"
            ],
            "56.00\n"
        ),
        (
            [
                "2",
                "Harsh 25 26.5 28",
                "Anurag 26 28 30",
                "Harsh"
            ],
            "26.50\n"
        ),
    ]
)

def test_finding_percentage(monkeypatch, capsys, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(input_iter))
    finding_percentage()
    captured = capsys.readouterr()
    assert captured.out == expected