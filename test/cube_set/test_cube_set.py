from src.cube_set.util import can_stack_cubes
import pytest

def test_piling_up_case_1():
    cubes = [4, 3, 2, 1, 3, 4]
    assert can_stack_cubes(cubes) == "Yes"

def test_piling_up_case_2():
    cubes = [1, 3, 2]
    assert can_stack_cubes(cubes) == "No"

def test_piling_up_case_3():
    cubes = [1]
    assert can_stack_cubes(cubes) == "Yes"

def test_piling_up_case_4():
    cubes = [5, 4, 3, 2, 1]
    assert can_stack_cubes(cubes) == "Yes"