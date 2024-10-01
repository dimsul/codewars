import pytest

from kyu_6.unique_in_order import unique_in_order


input_params = (('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
                ('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']),
                ([1, 2, 2, 3, 3], [1, 2, 3]),
                ((1, 2, 2, 3, 3), [1, 2, 3]),
                ("", []),
                ([], []),
                ((), []),
                ("A", ["A"]),
                (['A'], ['A']),
                (('A',), ['A']),
                ('AA', ['A']),
                ('AAAABBBCCDAABBB', ["A", "B", "C", "D", "A", "B"]),
                ("ABBCcA", ["A", "B", "C", "c", "A"]),
                ([1, 2, 3, 3, -1], [1, 2, 3, -1]),
                (["a", "b", "b", "a"], ["a", "b", "a"]))


@pytest.mark.kyu_6
@pytest.mark.algorithms
@pytest.mark.fundamentals
@pytest.mark.parametrize('sequence, exp_list', input_params)
def test_unique_in_order(sequence, exp_list):

    result = unique_in_order(sequence)

    assert result == exp_list
