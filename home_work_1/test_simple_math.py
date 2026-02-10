from simple_math import SimpleMath
import pytest

@pytest.fixture
def get_simple_math():
    return SimpleMath()

def test_simple_math_square(get_simple_math):
    assert get_simple_math.square(2) == 4

def test_simple_math_cube(get_simple_math):
    assert get_simple_math.cube(-3) == -27
