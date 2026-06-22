from src.string_formate.util import print_formatted
import pytest

@pytest.mark.parametrize(
    "number, expected_output",
    [
        (
            2,
            "1   1   1   1\n"
            "2   2   2   10\n"
        ),
        (
            5,
            "1   1   1   1\n"
            "2   2   2   10\n"
            "3   3   3   11\n"
            "4   4   4   100\n"
            "5   5   5   101\n"
        )
    ]
)

def test_print_formatted(capsys, number, expected_output):
    print_formatted(number)
    captured = capsys.readouterr()
    assert captured.out == expected_output