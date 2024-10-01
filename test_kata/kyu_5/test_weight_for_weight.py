import pytest

from kyu_5.weight_for_weight import order_weight


test_data = (("56 65 74 100 99 68 86 180 90", "100 180 90 56 65 74 68 86 99"),
             ("103 123 4444 99 2000", "2000 103 123 4444 99"),
             ("2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999"),
             ("", ""),)


@pytest.mark.kyu_5
@pytest.mark.algorithms
@pytest.mark.parametrize('strng, exp_res', test_data)
def test_order_weight(strng, exp_res):
    result = order_weight(strng)
    assert result == exp_res
