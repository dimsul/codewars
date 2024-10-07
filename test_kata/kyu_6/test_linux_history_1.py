import pytest

from kyu_6.linux_history_1 import bang_bang


test_data = (("   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me\n  7  more me\n  8  history", "history"),
             ("   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me\n  7  history\n  8  more me", "more me"),
             ("   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me\n  7  history\n  8  more me", "more me"),
             ("   1  touch me\n  2  cd /pub\n  3  more me\n  4  cd ..\n  5  chmod 000 me\n  6  more beer\n  7  lost\n  8  touch me\n  9  cd /pub\n  10  more me\n  11  cd ..\n  12  chmod 000 me\n  13  more beer\n  14  lost\n  15  touch me\n  16  cd /pub\n  17  more me\n  18  cd ..\n  19  chmod 000 me\n  20  more beer\n  21  lost", "lost"),
             ("   1  touch me\n  2  cd ..\n  3  more me\n  4  cd ..\n  5  chmod 000 me\n  6  more beer\n  7  lost\n  8  touch me\n  9  cd /pub\n  10  more me\n  11  cd ..\n  12  chmod 000 me\n  13  more beer\n  14  lost\n  15  touch me\n  16  cd /pub\n  17  more me\n  18  cd ..\n  19  chmod 000 me\n  20  more beer\n  21  lost\n  22  cd /pub", "cd /pub"),
             ("   1  touch me\n  2  cd ..\n  3  more me\n  4  cd ..\n  5  chmod 000 me\n  6  more beer\n  7  lost\n  8  touch me\n  9  cd /pub\n  10  more me\n  11  cd ..\n  12  chmod 000 me\n  13  more beer\n  14  lost\n  15  touch me\n  16  cd /pub\n  17  more me\n  18  cd ..\n  19  chmod 000 me\n  20  more beer\n  21  lost\n  22  cd /pub", 'cd /pub'),
             ('   1  cd /pub', 'cd /pub'))


@pytest.mark.kyu_6
@pytest.mark.strings
@pytest.mark.parsing
@pytest.mark.regular_expressions
@pytest.mark.algorithms
@pytest.mark.parametrize('history, exp_result', test_data)
def test_bang_bang(history, exp_result):
    result = bang_bang(history)
    assert result == exp_result
