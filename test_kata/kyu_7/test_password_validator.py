import pytest


from kyu_7.password_validator import password


test_data = (("Abcd1234", True),
             ("Abcd123", False),
             ("abcd1234", False),
             ("AbcdefGhijKlmnopQRsTuvwxyZ1234567890", True),
             ("ABCD1234", False),
             (r"Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,", True),
             (r"!@#$%^&*()-_+={}[]|\:;?/>.<,", False),
             ("", False),
             (" aA1----", True),
             ("4aA1----", True),)


@pytest.mark.parametrize('st, exp_result', test_data)
def test_password(st, exp_result):
    result = password(st)
    assert result == exp_result
