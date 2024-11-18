import pytest

from kyu_4.ranking_poker_hands import PokerHand


test_data = (("Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS"),
             ("Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD"),
             ("Win",  "AS AH 2H AD AC", "JS JD JC JH 3D"),
             ("Loss", "2S AH 2H AS AC", "JS JD JC JH AD"),
             ("Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H"),
             ("Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H"),
             ("Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C"),
             ("Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S"),
             ("Win",  "2S 3H 4H 5S AD", "AH AC 5H 6H AS"),
             ("Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS"),
             ("Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S"),
             ("Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S"),
             ("Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S"),
             ("Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S"),
             ("Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC"),
             ("Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C"),)


@pytest.mark.parametrize('exp_res, hand_1, hand_2', test_data)
def test_ranking_poker_hands(exp_res, hand_1, hand_2):
    result = PokerHand(hand_1).compare_with(PokerHand(hand_2))
    assert result == exp_res
