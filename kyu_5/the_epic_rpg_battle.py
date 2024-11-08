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

    def play_turn(self, act_1, act_2):
        # your code here
        pass


assassin = Assassin()
print(assassin.power)
assassin.buff()
print(assassin.power)
print(assassin.normal_attack())
print(assassin.power)
print(assassin.normal_attack())
print(assassin.power)
print(assassin.special_attack())
print(assassin.power)
print(assassin.special_attack())
print(assassin.power)
