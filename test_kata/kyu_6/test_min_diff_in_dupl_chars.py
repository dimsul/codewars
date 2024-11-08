import pytest

from kyu_6.min_diff_in_dupl_chars import min_repeating_character_difference


test_data = (('aabbca', (1, 'a')),
             ('abded', (2, 'd')),
             ('abbbbbc', (1, 'b')),
             ('aa', (1, 'a')),
             ('aba', (2, 'a')),
             ('osmdioudgfoglkdcfeokiydivkf', (3, 'g')))


@pytest.mark.kyu_6
@pytest.mark.strings
@pytest.mark.parametrize('text, exp_res', test_data)
def test_min_repeating_character_difference(text, exp_res):
    result = min_repeating_character_difference(text)
    assert result == exp_res
