import pytest


@pytest.fixture(scope='session', autouse=True)
def import_modules():
    from kyu_6 import unique_in_order
