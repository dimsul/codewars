from enum import Enum


class Actions(Enum):
    BUFF = 1
    NORMAL_ATTACK = 2
    SPECIAL_ATTACK = 3


class Warrior:
    def __init__(self):
        self.hp = 260
        self.power = 40
        self.buff_activ = False
        self.name = 'Warrior'

    def normal_attack(self):
        return self.power

    def special_attack(self):
        return self.power + 35

    def buff(self):
        self.buff_activ = True
        self.hp = self.hp + 40 if self.hp + 40 <= 260 else 260
        return 0

    def acc_dmg(self, power):
        if not self.buff_activ:
            self.hp = self.hp - power
        else:
            self.hp = self.hp - power // 2
            self.buff_activ = False


class Mage:
    def __init__(self):
        self.hp = 200
        self.power = 50
        self.buff_active = False
        self.name = 'Mage'

    def normal_attack(self):
        return self.power

    def special_attack(self):
        return self.power + 40

    def buff(self):
        self.buff_active = True
        return 0

    def acc_dmg(self, power):
        if not self.buff_active:
            self.hp = self.hp - power
        else:
            self.buff_active = False


class Assassin:
    def __init__(self):
        self.hp = 235
        self.power = 30
        self.buff_active = 0
        self.name = 'Assassin'

    def normal_attack(self):
        self.__check_buff()
        return self.power

    def special_attack(self):
        self.__check_buff()
        return self.power * 2

    def buff(self):
        self.buff_active = 3
        self.power += 40
        return 0

    def __check_buff(self):
        if self.buff_active:
            self.buff_active -= 1
            return
        self.power = 30

    def acc_dmg(self, power):
        self.hp -= power


class Battle:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.battle_in_action = True

    def play_turn(self, act_1, act_2):
        if not self.battle_in_action:
            return 'This battle is over!'
        else:
            self.__action(act_1, self.player_1, self.player_2)
            if self.__check_winner():
                return self.__check_winner()
            self.__action(act_2, self.player_2, self.player_1)
            if self.__check_winner():
                return self.__check_winner()
            return f'{self.player_1.name} HP {self.player_1.hp}, {self.player_2.name} HP {self.player_2.hp}'

    def __check_winner(self):
        if self.player_1.hp <= 0:
            self.battle_in_action = False
            return f'The {self.player_2.name} won! Remaining HP = {self.player_2.hp}'
        elif self.player_2.hp <= 0:
            self.battle_in_action = False
            return f'The {self.player_1.name} won! Remaining HP = {self.player_1.hp}'

        return None

    @staticmethod
    def __action(act, pl_1, pl_2):
        if act.value == 1:
            pl_1.buff()
        elif act.value == 2:
            act_res = pl_1.normal_attack()
            pl_2.acc_dmg(act_res)
        elif act.value == 3:
            act_res = pl_1.special_attack()
            pl_2.acc_dmg(act_res)


plr_1 = Assassin()
plr_2 = Mage()
epic_battle = Battle(plr_1, plr_2)
print(epic_battle.play_turn(Actions.BUFF, Actions.BUFF))
print(epic_battle.play_turn(Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK))
print(epic_battle.play_turn(Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK))
print(epic_battle.play_turn(Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK))
print(epic_battle.play_turn(Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK))
