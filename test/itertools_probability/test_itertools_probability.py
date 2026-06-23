from src.itertools_probability.util import probability_of_a

def test_probability_case_1():
    result = probability_of_a(
        ["a", "a", "c", "d"],
        2
    )
    assert round(result, 4) == 0.8333

def test_probability_case_2():
    result = probability_of_a(
        ["a", "b", "c"],
        2
    )
    assert round(result, 4) == 0.6667

def test_probability_case_3():
    result = probability_of_a(
        ["b", "c", "d"],
        2
    )
    assert result == 0.0