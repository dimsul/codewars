import pytest


from kyu_7.regex_validate_pin_code import validate_pin


test_data = (('1', False),
             ('12', False),
             ('123', False),
             ('12345', False),
             ('1234567', False),
             ('-1234', False),
             ('-12345', False),
             ('1.234', False),
             ('00000000', False),
             ('a234', False),
             ('.234', False),
             ('1234', True),
             ('0000', True),
             ('123456', True),
             ('000000', True),
             ('1111', True),
             ('056789', True),
             ('125498', True),
             ('090909', True),)


@pytest.mark.kyu_7
@pytest.mark.fundamentals
@pytest.mark.regular_expressions
@pytest.mark.parametrize("pin, exp_res", test_data)
def test_validate_pin(pin, exp_res):
    result = validate_pin(pin)
    assert result == exp_res
