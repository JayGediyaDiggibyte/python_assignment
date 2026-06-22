from src.merge_tool.util import merge_the_tools
import pytest

@pytest.mark.parametrize(
    "string, k, expected",
    [
        (
            "AABCAAADA",
            3,
            "AB\nCA\nAD\n"
        ),
        (
            "AAABBBCCC",
            3,
            "A\nB\nC\n"
        )
    ]
)

def test_merge_the_tools(capsys, string, k, expected):
    merge_the_tools(string, k)
    captured = capsys.readouterr()
    assert captured.out == expected