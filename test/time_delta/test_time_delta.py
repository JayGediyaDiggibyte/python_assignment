from src.time_delta.util import time_delta
import pytest

def test_time_delta_case_1():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
    assert time_delta(t1, t2) == "25200"

def test_time_delta_case_2():
    t1 = "Sat 02 May 2015 19:54:36 +0530"
    t2 = "Fri 01 May 2015 13:54:36 -0000"
    assert time_delta(t1, t2) == "88200"