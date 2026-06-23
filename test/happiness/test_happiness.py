from src.happiness.util import calculate_happiness
import pytest

def test_happiness_case_1():
    arr = [1, 5, 3]
    liked = {3, 1}
    disliked = {5, 7}
    assert calculate_happiness(arr, liked, disliked) == 1