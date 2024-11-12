# Task
# Your task is to create a class called Battle and also
# the characters that will be part of the battle.
# The class should take two of these character objects
# when initialized and include a method named play_turn
# to handle the actions taken during each turn.
#
# The characters have attributes and abilities and you
# should implemente them according to the descriptions
# provided below. There are three character classes
# Warrior, Mage, Assassin:
#
# The characters can execute one of the three actions per turn:
#
# Buff, temporary effects that enhance attributes or abilities.
# Normal attack, inflicting damage equals to the attack power
# (assassins can modify this value).
# Special attack, an ability that deals more damage than normal.

# The test cases will call the method play_turn, and two of these
# constants will be passed as arguments. The first (act_1) must
# correspond to the action of the first character passed when
# instantiating the Battle object, and the second (act_2) for
# the second character.
#
# The first character executes their action first, giving them
# an advantage in the battle.
#
# Furthermore the characters maybe receive damage originating of
# your adversary, and you must implement this taking into account
# each character's abilities and attributes.
# Returns
# After completing the characters' actions, the method play_turn must return:
#
# The winning character with your current HP when the opponent's HP
# is reduced to 0 this turn, exemples: "The Warrior won! Remaining HP = 50",
# "The Mage won! Remaining HP = 30" or "The Assassin won! Remaining HP = 95".
# "This battle is over!" for other play_turn calls after one of the characters
# has their hp reduced to 0.
# In the other cases, the only respective hp of the classes after the
# actions: "Warrior HP = 210, Mage HP = 160"
#
# Some Rules and Considerations
# 1. The warrior does not regenerate more than his maximum hp, in this case 260.
# 2. The only way for a warrior or mage to lose their buff effects is by
#    suffering an attack from the opponent, whether normal or special.
# 3. The shield of mage absorbes only one attack, after that, the shield
#    will be consumed.
# 4. In a similar way, iron skin of warrior, reduces only one attack.
# 5. Remember that the assassin increases his power, and this influences
#    the damage of the lacerate and normal attack.
# 6. Assassin's instinct lasts for three attacks, and each attack consumes
#    one charge.
# 7. Buffs do not stack, for example: The wizard cannot have more than one
#    shield, and the assassin cannot have more than 3 charges. However, if
#    the assassin uses assassin's instinct while he still has charges remaining,
#    they will be renewed. The warrior can heal whenever he uses iron skin, even
#    if its effect is active.
# 8. Consider only the integer part when performing calculations.


from enum import Enum


class Actions(Enum):
    BUFF = 1
    NORMAL_ATTACK = 2
    SPECIAL_ATTACK = 3


class Warrior:
    def __init__(self):
        """
        Warrior
        """

        self.hp = 260
        self.power = 40
        self.buff_activ = False
        self.name = 'Warrior'

    def normal_attack(self) -> int:
        """
        Normal attack
        """

        return self.power

    def special_attack(self) -> int:
        """
        Special attack
        """

        return self.power + 35

    def buff(self) -> None:
        """
        Getting a buff
        """

        self.buff_activ = True
        self.hp = self.hp + 40 if self.hp + 40 <= 260 else 260

    def acc_dmg(self, power) -> None:
        """
        Taking damage
        :param power:  damage
        """

        if not self.buff_activ:

            self.hp = self.hp - power

        else:

            self.hp = self.hp - (power // 2)
            self.buff_activ = False


class Mage:
    def __init__(self):
        """
        Mage
        """

        self.hp = 200
        self.power = 50
        self.buff_active = False
        self.name = 'Mage'

    def normal_attack(self) -> int:
        """
        Normal attack
        """

        return self.power

    def special_attack(self) -> int:
        """
        Special attack
        """

        return self.power + 40

    def buff(self) -> None:
        """
        Getting a buff
        """

        self.buff_active = True

    def acc_dmg(self, power) -> None:
        """
        Taking damage
        :param power:  damage
        """

        if not self.buff_active:
            self.hp = self.hp - power

        else:
            self.buff_active = False


class Assassin:
    def __init__(self):
        """
        Assassin
        """

        self.hp = 235
        self.power = 30
        self.buff_active = 0
        self.name = 'Assassin'

    def normal_attack(self) -> int:
        """
        Normal attack
        """

        self.__check_buff()
        return self.power

    def special_attack(self) -> int:
        """
        Special attack
        """

        self.__check_buff()
        return self.power * 2

    def buff(self) -> None:
        """
        Getting a buff
        """

        self.buff_active = 3
        self.power = 70

    def __check_buff(self) -> None:
        """
        Check buff
        """

        if self.buff_active:
            self.buff_active -= 1
            return

        self.power = 30

    def acc_dmg(self, power) -> None:
        """
        Taking damage
        :param power:  damage
        """

        self.hp -= power


class Battle:

    def __init__(self, player_1, player_2):
        """
        Battle
        :param player_1: player #1
        :param player_2: player #2
        """

        self.player_1 = player_1
        self.player_2 = player_2
        self.battle_in_action = True

    def play_turn(self, act_1, act_2) -> str:
        """
        Play one turn
        :param act_1: action for player #1
        :param act_2: action for player #2
        """

        if not self.battle_in_action:
            return 'This battle is over!'

        else:

            self.__action(act_1, self.player_1, self.player_2)
            if self.__check_winner():
                return self.__check_winner()

            self.__action(act_2, self.player_2, self.player_1)
            if self.__check_winner():
                return self.__check_winner()

            return f'{self.player_1.name} HP = {self.player_1.hp}, {self.player_2.name} HP = {self.player_2.hp}'

    def __check_winner(self) -> str | None:
        """
        Check for winner
        """

        if self.player_1.hp <= 0:
            self.battle_in_action = False
            return f'The {self.player_2.name} won! Remaining HP = {self.player_2.hp}'

        elif self.player_2.hp <= 0:
            self.battle_in_action = False
            return f'The {self.player_1.name} won! Remaining HP = {self.player_1.hp}'

        return None

    @staticmethod
    def __action(act, pl_1, pl_2) -> None:
        """
        Make action for both players
        :param act: action
        :param pl_1: player who performs the action
        :param pl_2: player who takes damage
        """

        if act.value == 1:
            pl_1.buff()

        elif act.value == 2:
            act_res = pl_1.normal_attack()
            pl_2.acc_dmg(act_res)

        elif act.value == 3:
            act_res = pl_1.special_attack()
            pl_2.acc_dmg(act_res)
