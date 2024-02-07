import pytest
from core.main import sum, is_greater_than, login

def test_sum():
    assert sum(2, 5) == 7

def test_is_greater_than():
    assert is_greater_than(10, 2)

@pytest.mark.parametrize(
    'inp_x, inp_y, expected',
    [
        (5,1,6),
        (6,sum(4,2),12),
        (sum(19,1),15,35),
        (-7,10,sum(-7, 10))
    ]
)
def test_sum_params(inp_x, inp_y, expected):
    assert sum(inp_x, inp_y) == expected

def test_login_pass():
    login_pass = login('leonfio', '123456')
    assert login_pass

def test_login_fail():
    login_fail = login('leonfio', '654321')
    assert not login_fail