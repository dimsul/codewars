import pytest

from kyu_5.the_epic_rpg_battle import Actions, Warrior, Mage, Assassin, Battle


assassin_vs_mage_test_data = ((Actions.BUFF, Actions.BUFF, 'Assassin HP = 235, Mage HP = 200'),
                              (Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'Assassin HP = 145, Mage HP = 200'),
                              (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Assassin HP = 95, Mage HP = 130'),
                              (Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'The Assassin won! Remaining HP = 95'),
                              (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'This battle is over!'))

mage_vs_assassin_test_data = ((Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'Mage HP = 140, Assassin HP = 145'),
                              (Actions.BUFF, Actions.NORMAL_ATTACK, 'Mage HP = 140, Assassin HP = 145'),
                              (Actions.BUFF, Actions.BUFF, 'Mage HP = 140, Assassin HP = 145'),
                              (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Mage HP = 140, Assassin HP = 95'),
                              (Actions.SPECIAL_ATTACK, Actions.NORMAL_ATTACK, 'Mage HP = 70, Assassin HP = 5'),
                              (Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'The Mage won! Remaining HP = 70'),
                              (Actions.BUFF, Actions.SPECIAL_ATTACK, 'This battle is over!'))

warrior_vs_mage_test_data = ((Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Warrior HP = 210, Mage HP = 160'),
                             (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Warrior HP = 160, Mage HP = 120'),
                             (Actions.NORMAL_ATTACK, Actions.BUFF, 'Warrior HP = 160, Mage HP = 80'),
                             (Actions.SPECIAL_ATTACK, Actions.NORMAL_ATTACK, 'Warrior HP = 110, Mage HP = 80'),
                             (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Warrior HP = 60, Mage HP = 40'),
                             (Actions.NORMAL_ATTACK, Actions.SPECIAL_ATTACK, 'The Warrior won! Remaining HP = 60'),
                             (Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'This battle is over!'))

mage_vs_warrior_test_data = ((Actions.BUFF, Actions.NORMAL_ATTACK, 'Mage HP = 200, Warrior HP = 260'),
                             (Actions.BUFF, Actions.NORMAL_ATTACK, 'Mage HP = 200, Warrior HP = 260'),
                             (Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'Mage HP = 125, Warrior HP = 170'),
                             (Actions.BUFF, Actions.NORMAL_ATTACK, 'Mage HP = 125, Warrior HP = 170'),
                             (Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'Mage HP = 50, Warrior HP = 80'),
                             (Actions.SPECIAL_ATTACK, Actions.NORMAL_ATTACK, 'The Mage won! Remaining HP = 50'),
                             (Actions.NORMAL_ATTACK, Actions.BUFF, 'This battle is over!'))

assassin_vs_warrior_test_data = ((Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Assassin HP = 195, Warrior HP = 230'),
                                 (Actions.BUFF, Actions.BUFF, 'Assassin HP = 195, Warrior HP = 260'),
                                 (Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK, 'Assassin HP = 120, Warrior HP = 190'),
                                 (Actions.NORMAL_ATTACK, Actions.BUFF, 'Assassin HP = 120, Warrior HP = 160'),
                                 (Actions.SPECIAL_ATTACK, Actions.NORMAL_ATTACK, 'Assassin HP = 80, Warrior HP = 90'),
                                 (Actions.BUFF, Actions.BUFF, 'Assassin HP = 80, Warrior HP = 130'),
                                 (Actions.NORMAL_ATTACK, Actions.BUFF, 'Assassin HP = 80, Warrior HP = 135'),
                                 (Actions.NORMAL_ATTACK, Actions.BUFF, 'Assassin HP = 80, Warrior HP = 140'),
                                 (Actions.NORMAL_ATTACK, Actions.SPECIAL_ATTACK, 'Assassin HP = 5, Warrior HP = 105'),
                                 (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'The Warrior won! Remaining HP = 75'))

warrior_vs_assassin_test_data = ((Actions.BUFF, Actions.NORMAL_ATTACK, 'Warrior HP = 245, Assassin HP = 235'),
                                 (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Warrior HP = 215, Assassin HP = 195'),
                                 (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Warrior HP = 185, Assassin HP = 155'),
                                 (Actions.BUFF, Actions.NORMAL_ATTACK, 'Warrior HP = 210, Assassin HP = 155'),
                                 (Actions.SPECIAL_ATTACK, Actions.BUFF, 'Warrior HP = 210, Assassin HP = 80'),
                                 (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'Warrior HP = 140, Assassin HP = 40'),
                                 (Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK, 'The Warrior won! Remaining HP = 140'),
                                 (Actions.BUFF, Actions.SPECIAL_ATTACK, 'This battle is over!'))


@pytest.fixture(scope='session')
def assassin_vs_mage_battle_prep():
    player_1 = Assassin()
    player_2 = Mage()
    epic_battle = Battle(player_1, player_2)
    return epic_battle


@pytest.fixture(scope='session')
def mage_vs_assassin_battle_prep():
    player_1 = Mage()
    player_2 = Assassin()
    epic_battle = Battle(player_1, player_2)
    return epic_battle


@pytest.fixture(scope='session')
def warrior_vs_mage_battle_prep():
    player_1 = Warrior()
    player_2 = Mage()
    epic_battle = Battle(player_1, player_2)
    return epic_battle


@pytest.fixture(scope='session')
def mage_vs_warrior_battle_prep():
    player_1 = Mage()
    player_2 = Warrior()
    epic_battle = Battle(player_1, player_2)
    return epic_battle


@pytest.fixture(scope='session')
def assassin_vs_warrior_battle_prep():
    player_1 = Assassin()
    player_2 = Warrior()
    epic_battle = Battle(player_1, player_2)
    return epic_battle


@pytest.fixture(scope='session')
def warrior_vs_assassin_battle_prep():
    player_1 = Warrior()
    player_2 = Assassin()
    epic_battle = Battle(player_1, player_2)
    return epic_battle


@pytest.mark.kyu_5
@pytest.mark.object_oriented_programming
@pytest.mark.games
@pytest.mark.the_epic_rpg_battle
@pytest.mark.parametrize('act_1, act_2, exp_res', assassin_vs_mage_test_data)
def test_assassin_vs_mage_battle(assassin_vs_mage_battle_prep, act_1, act_2, exp_res):
    epic_battle = assassin_vs_mage_battle_prep
    result = epic_battle.play_turn(act_1, act_2)
    assert result == exp_res


@pytest.mark.kyu_5
@pytest.mark.object_oriented_programming
@pytest.mark.games
@pytest.mark.the_epic_rpg_battle
@pytest.mark.parametrize('act_1, act_2, exp_res', mage_vs_assassin_test_data)
def test_mage_vs_assassin_battle(mage_vs_assassin_battle_prep, act_1, act_2, exp_res):
    epic_battle = mage_vs_assassin_battle_prep
    result = epic_battle.play_turn(act_1, act_2)
    assert result == exp_res


@pytest.mark.kyu_5
@pytest.mark.object_oriented_programming
@pytest.mark.games
@pytest.mark.the_epic_rpg_battle
@pytest.mark.parametrize('act_1, act_2, exp_res', warrior_vs_mage_test_data)
def test_warrior_vs_mage_battle(warrior_vs_mage_battle_prep, act_1, act_2, exp_res):
    epic_battle = warrior_vs_mage_battle_prep
    result = epic_battle.play_turn(act_1, act_2)
    assert result == exp_res


@pytest.mark.kyu_5
@pytest.mark.object_oriented_programming
@pytest.mark.games
@pytest.mark.the_epic_rpg_battle
@pytest.mark.parametrize('act_1, act_2, exp_res', mage_vs_warrior_test_data)
def test_mage_vs_warrior_battle(mage_vs_warrior_battle_prep, act_1, act_2, exp_res):
    epic_battle = mage_vs_warrior_battle_prep
    result = epic_battle.play_turn(act_1, act_2)
    assert result == exp_res


@pytest.mark.kyu_5
@pytest.mark.object_oriented_programming
@pytest.mark.games
@pytest.mark.the_epic_rpg_battle
@pytest.mark.parametrize('act_1, act_2, exp_res', assassin_vs_warrior_test_data)
def test_assassin_vs_warrior_battle(assassin_vs_warrior_battle_prep, act_1, act_2, exp_res):
    epic_battle = assassin_vs_warrior_battle_prep
    result = epic_battle.play_turn(act_1, act_2)
    assert result == exp_res


@pytest.mark.kyu_5
@pytest.mark.object_oriented_programming
@pytest.mark.games
@pytest.mark.the_epic_rpg_battle
@pytest.mark.parametrize('act_1, act_2, exp_res', warrior_vs_assassin_test_data)
def test_warrior_vs_assassin_battle(warrior_vs_assassin_battle_prep, act_1, act_2, exp_res):
    epic_battle = warrior_vs_assassin_battle_prep
    result = epic_battle.play_turn(act_1, act_2)
    assert result == exp_res
