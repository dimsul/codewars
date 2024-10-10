import pytest

from kyu_6.ip_validation import is_valid_ip


input_data = (('12.255.56.1', True),
              ('', False),
              ('abc.def.ghi.jkl', False),
              ('123.456.789.0', False),
              ('12.34.56', False),
              ('12.34.56 .1', False),
              ('12.34.56.-1', False),
              ('123.045.067.089', False),
              ('127.1.1.0', True),
              ('0.0.0.0', True),
              ('0.34.82.53', True),
              ('192.168.1.300', False),
              ('1.2.3.4\n', False),
              ('0.34.82.102', True))


@pytest.mark.algorithms
@pytest.mark.regular_expressions
@pytest.mark.parametrize('string, exp_result', input_data)
def test_is_valid_ip(string, exp_result):
    result = is_valid_ip(string)
    assert result == exp_result
