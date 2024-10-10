import pytest


from kyu_6.split_string import solution


test_data = (("asdfadsf", ['as', 'df', 'ad', 'sf']),
             ("asdfads", ['as', 'df', 'ad', 's_']),
             ("", []),
             ("x", ["x_"]),)


@pytest.mark.algorithms
@pytest.mark.strings
@pytest.mark.regular_expressions
@pytest.mark.parametrize('s, exp_result', test_data)
def test_solution(s, exp_result):
    result = solution(s)
    assert result == exp_result
