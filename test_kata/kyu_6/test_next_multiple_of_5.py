import pytest

from kyu_6.next_multiple_of_5 import next_multiple_of_five, next_multiple_of_five_2


test_data = ((5, 10),
             (8, 35),
             (2, 5),
             (13, 55),
             (27, 55),)


@pytest.mark.kyu_6
@pytest.mark.algorithms
@pytest.mark.logic
@pytest.mark.performance
@pytest.mark.parametrize('n, exp_result', test_data)
def test_next_multiple_of_five(n, exp_result):
    result = next_multiple_of_five(n)
    assert result == exp_result


@pytest.mark.kyu_6
@pytest.mark.algorithms
@pytest.mark.logic
@pytest.mark.performance
@pytest.mark.parametrize('n, exp_result', test_data)
def test_next_multiple_of_five_2(n, exp_result):
    result = next_multiple_of_five_2(n)
    assert result == exp_result
