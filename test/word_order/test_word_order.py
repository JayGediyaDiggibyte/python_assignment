from src.word_order.util import word_order
import pytest

def test_word_order_case_1():
    count, occurrences = word_order(
        [
            "bcdef",
            "abcdefg",
            "bcde",
            "bcdef"
        ]
    )
    assert count == 3
    assert occurrences == [2, 1, 1]

def test_word_order_case_2():
    count, occurrences = word_order(
        [
            "apple",
            "apple",
            "apple"
        ]
    )
    assert count == 1
    assert occurrences == [3]

def test_word_order_case_3():
    count, occurrences = word_order(
        [
            "a",
            "b",
            "c"
        ]
    )
    assert count == 3
    assert occurrences == [1, 1, 1]