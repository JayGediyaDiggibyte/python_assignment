from src.text_alignment.util import text_alignment
import pytest

@pytest.mark.parametrize(
    "thickness, first_line",
    [
        (3, "  H"),
        (5, "    H"),
    ]
)

def test_top_cone(thickness, first_line, capsys):
    text_alignment(thickness)
    captured = capsys.readouterr()
    assert captured.out.splitlines()[0].startswith(first_line)