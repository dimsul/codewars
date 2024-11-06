import pytest

from kyu_8.replace_all_dots import replace_dots


test_data = (('', ''),
             ('no dots', 'no dots'),
             ('one.two.three', 'one-two-three'),
             ('........', '--------'),
             ('x..x..x.xx...', 'x--x--x-xx---'),
             ('.....x.xx..xx', '-----x-xx--xx'),
             ('...xxxx...xx..', '---xxxx---xx--'),
             ('xx.x..xx.x.x.x.xx.x', 'xx-x--xx-x-x-x-xx-x'),)


@pytest.mark.kyu_8
@pytest.mark.debugging
@pytest.mark.regular_expressions
@pytest.mark.parametrize('s, exp_res', test_data)
def test_replace_dots(s, exp_res):
    result = replace_dots(s)
    assert result == exp_res
