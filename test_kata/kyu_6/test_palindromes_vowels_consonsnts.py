import pytest

from kyu_6.palindromes_vowels_consonsnts import palindrome


test_data = (('egg', 'both'),
             ('raCe car', 'both'),
             ('wizard', 'neither'),
             ('pea13ce', 'vowel'),
             (' *73_ ab', 'both'),
             ('3-B0oto b', 'both'),
             ('_inte 4', 'neither'),
             ('neither', 'vowel'),
             ('A man, a plan, a canal: Panama', 'both'),
             ('rotar', 'consonant'))


@pytest.mark.parametrize('s, exp_res', test_data)
def test_palindrome(capsys, s, exp_res):
    result = palindrome(s)
    assert result == exp_res
