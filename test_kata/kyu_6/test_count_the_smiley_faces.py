import pytest

from kyu_6.count_the_smiley_faces import count_smileys


test_data = (([], 0),
             ([':D', ':~)', ';~D', ':)'], 4),
             ([':)', ':(', ':D', ':O', ':;'], 2),
             ([';]', ':[', ';*', ':$', ';-D'], 1),
             ([';]', ':', ')', ':$', ';-D'], 1),
             ([':-(', ':(', ';-(', ':-(', ':-('], 0),
             ([':(', ':(', ';-D', ';-(', ';D', ';(', ';(', ':(', ';(', ';D', ';o(', ':-D', ';o(', ';('], 4),
             ([';(', ':oD', ':(', ':(', ':o(', ':-('], 0))


@pytest.mark.kyu_6
@pytest.mark.fundamentals
@pytest.mark.regular_expressions
@pytest.mark.parametrize('arr, exp_res', test_data)
def test_count_smiley(arr, exp_res):
    result = count_smileys(arr)
    assert result == exp_res
