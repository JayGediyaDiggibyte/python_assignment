from src.week_day.utli import find_day
import pytest

def test_find_day_wednesday():
    assert find_day(8, 5, 2026) == "WEDNESDAY"

def test_find_day_saturday():
    assert find_day(1, 3, 2026) == "SATURDAY"

def test_find_day_friday():
    assert find_day(12, 25, 2026) == "FRIDAY"

def test_find_day_leap_year():
    assert find_day(2, 29, 2024) == "THURSDAY"