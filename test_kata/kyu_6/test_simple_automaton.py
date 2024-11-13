import pytest

from kyu_6.simple_automaton import Automaton


test_data = ((['1'], True),
             (['1', '0'], False),
             (['1', '0', '1'], True),
             (['1', '0', '0'], True),
             (['0', '0', '1', '1', '0', '1', '1', '0'], False),)


@pytest.fixture(scope='session')
def prepare_automaton():
    return Automaton()


@pytest.mark.kyu_6
@pytest.mark.algorithms
@pytest.mark.state_machines
@pytest.mark.artificial_intelligence
@pytest.mark.object_oriented_programming
@pytest.mark.parametrize('commands, exp_res', test_data)
def test_automaton(prepare_automaton, commands, exp_res):
    my_automaton = prepare_automaton
    result = my_automaton.read_commands(commands)
    assert result == exp_res
