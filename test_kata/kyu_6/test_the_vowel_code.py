import pytest

from kyu_6.the_vowel_code import encode, decode


test_data_encode = (('hello', 'h2ll4'),
                    ('How are you today?', 'H4w 1r2 y45 t4d1y?'),
                    ('This is an encoding test.', 'Th3s 3s 1n 2nc4d3ng t2st.'),
                    ('hi there', 'h3 th2r2'),)

test_data_decode = (('h2ll4', 'hello'),
                    ('H4w 1r2 y45 t4d1y?', 'How are you today?'),
                    ('Th3s 3s 1n 2nc4d3ng t2st.', 'This is an encoding test.'),
                    ('h3 th2r2', 'hi there'),)


@pytest.mark.kyu_6
@pytest.mark.arrays
@pytest.mark.strings
@pytest.mark.regular_expressions
@pytest.mark.fundamentals
@pytest.mark.parametrize('st, exp_result', test_data_encode)
def test_encode(st, exp_result):
    result = encode(st)
    assert result == exp_result


@pytest.mark.kyu_6
@pytest.mark.arrays
@pytest.mark.strings
@pytest.mark.regular_expressions
@pytest.mark.fundamentals
@pytest.mark.parametrize('st, exp_result', test_data_decode)
def test_decode(st, exp_result):
    result = decode(st)
    assert result == exp_result
