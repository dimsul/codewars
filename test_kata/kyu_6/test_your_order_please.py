import pytest

from kyu_6.your_order_please import order


params = (("is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
          ("4of Fo1r pe6ople g3ood th5e the2", "Fo1r the2 g3ood 4of th5e pe6ople"),
          ("", ""),)


@pytest.mark.kyu_6
@pytest.mark.fundamentals
@pytest.mark.strings
@pytest.mark.parametrize('sentence, exp_result', params)
def test_your_order_please(sentence, exp_result):
    result = order(sentence)
    assert result == exp_result
