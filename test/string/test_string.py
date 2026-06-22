from src.string.util import mutate_string
import pytest

@pytest.mark.parametrize(
    "string, position, character, expected_output",
    [
        ("abracadabra", 5, "k", "abrackdabra"),
        ("hello", 0, "H", "Hello"),
        ("python", 3, "X", "pytXon"),
        ("test", 3, "T", "tesT"),
    ]
)

def test_mutate_string(string, position, character, expected_output):
    result = mutate_string(string, position, character)
    assert result == expected_output