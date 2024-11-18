# Task
#
# Create a poker hand that has a method to compare itself to another poker hand:
#
# compare_with(self, other_hand)
#
# A poker hand has a constructor that accepts a string containing 5 cards:
#
# PokerHand("KS 2H 5C JD TD")
#
# The characteristics of the string of cards are:
#
#     Each card consists of two characters, where
#     The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
#     The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
#     A space is used as card separator between cards
#
# The result of your poker hand compare can be one of these 3 options:
#
# [ "Win", "Tie", "Loss" ]
#
# Notes
#
#     Apply the Texas Hold'em rules for ranking the cards.
#     Low aces are valid in this kata.
#     There is no ranking for the suits.


class Hand:
    CARD_VALUE = '23456789TJQKA'

    @classmethod
    def get_card_value(cls, card):
        return cls.CARD_VALUE.index(card)


class HandHighCard(Hand):

    def __init__(self, sorted_hand):
        """
        Hand with high card
        :param sorted_hand: sorted values of card in hend
        """
        self.price = 0
        self.sorted_hand = sorted_hand

    def compare(self, hand) -> str:
        """
        Compare current hand with the other of the same class
        :param hand: enother high card hand
        """
        for i in range(len(self.sorted_hand)-1, -1, -1):
            if self.get_card_value(self.sorted_hand[i]) > self.get_card_value(hand.sorted_hand[i]):
                return 'Win'
            elif self.get_card_value(self.sorted_hand[i]) < self.get_card_value(hand.sorted_hand[i]):
                return 'Loss'

        return 'Tie'


class HandPair(HandHighCard):

    def __init__(self, card: str, sorted_hand: str):
        """
        Hand with pair
        :param card: value of pair cards
        :param sorted_hand: sorted values of card in hend
        """
        super().__init__(sorted_hand.replace(card, ''))
        self.price = 1
        self.card = card
        # self.sorted_hand = sorted_hand.replace(pair, '')

    def compare(self, hand) -> str:
        """
        Compare current hand with the other of the same class
        :param hand: enother card hand
        """
        if self.get_card_value(self.card) > self.get_card_value(hand.card):
            return 'Win'
        elif self.get_card_value(self.card) < self.get_card_value(hand.card):
            return 'Loss'

        return super().compare(hand)


class HandTwoPairs(HandHighCard):

    def __init__(self, pair_one: str, pair_two: str, sorted_hand: str):
        """
        Hand with two pairs
        :param pair_one: value of first pair card
        :param pair_two: value of second pair card
        :param sorted_hand: sorted values of card in hend
        """
        super().__init__(sorted_hand.replace(pair_one, '').replace(pair_two, ''))
        self.price = 2
        self.pair_values = (self.get_card_value(pair_one), self.get_card_value(pair_two))

    def compare(self, value) -> str:
        """
        Compare current hand with other two pairs hand
        :param value: enother card hand
        """
        if max(value.pair_values) > max(self.pair_values):
            return 'Loss'
        elif max(value.pair_values) < max(self.pair_values):
            return 'Win'
        else:
            if min(value.pair_values) > min(self.pair_values):
                return 'Loss'
            elif min(value.pair_values) < min(self.pair_values):
                return 'Win'

        return super().compare(value)


class HandThreeOfAKind(HandHighCard):

    def __init__(self, card: str, sorted_hand: str):
        """
        Hand with three of a kind
        :param card: value of tree cards
        :param sorted_hand: sorted values of card in hend
        """
        super().__init__(sorted_hand.replace(card, ''))
        self.price = 3
        self.card = card
        
    def compare(self, hand) -> str:
        """
        Compare current hand with the other of the same class
        :param hand: enother high card hand
        """
        if self.get_card_value(self.card) > self.get_card_value(hand.card):
            return 'Win'
        elif self.get_card_value(self.card) < self.get_card_value(hand.card):
            return 'Loss'
        
        return super().compare(hand)


class HandStraight(HandHighCard):

    def __init__(self, sorted_hand):
        super().__init__(sorted_hand)
        self.price = 4


class HandFlush(HandHighCard):

    def __init__(self, sorted_hand):
        super().__init__(sorted_hand)
        self.price = 5


class HandFullHouse(Hand):

    def __init__(self, three_of_a_kind: HandThreeOfAKind, pair: HandPair):
        """
        Hand with full house
        :param three_of_a_kind: Hand with three of a kind
        :param pair: Hand with pair
        """
        self.price = 6
        self.three_of_a_kind = three_of_a_kind
        self.pair = pair

    def compare(self, hand):
        if self.three_of_a_kind.card > hand.three_of_a_kind.card:
            return 'Win'
        elif self.three_of_a_kind.card < hand.three_of_a_kind.card:
            return "Loss"
        else:
            if self.pair.card > hand.pair.card:
                return 'Win'
            elif self.pair.card < hand.pair.card:
                return "Loss"
            else:
                return 'Tie'


class HandFourOfAKind(HandHighCard):
    def __init__(self, card, sorted_hand: str):
        super().__init__(sorted_hand.replace(card, ''))
        self.price = 7
        self.card = card

    def compare(self, hand) -> str:
        if self.get_card_value(self.card) > self.get_card_value(hand.card):
            return 'Win'
        elif self.get_card_value(self.card) < self.get_card_value(hand.card):
            return 'Loss'

        return super().compare(hand)


class HandStraightFlush(HandHighCard):

    def __init__(self, sorted_hand):
        super().__init__(sorted_hand)
        self.price = 8


class HandFlushRoyal(HandHighCard):

    def __init__(self, high_card):
        super().__init__(high_card)
        self.price = 9

    def compare(self, hand) -> str:
        return 'Tie'


class PokerHand:
    CARD_VALUE = '23456789TJQKA'

    def __init__(self, hand: str):
        self.__hand = hand
        self.__sorted_hand = self.__get_hand_value_sorted()
        self.hand_value = self.__get_hand_value()

    def compare_with(self, other):

        if self.hand_value.price > other.hand_value.price:
            return 'Win'
        elif self.hand_value.price < other.hand_value.price:
            return 'Loss'
        else:
            return self.hand_value.compare(other.hand_value)

    def __get_hand_suit(self):
        return ''.join(card[1] for card in self.__hand.split(' '))

    def __get_hand_value_sorted(self):
        """
        sorting hand in assending order by value
        """
        value = ''.join([card[0] for card in self.__hand.split(' ')])
        return ''.join(sorted(value, key=lambda a: self.CARD_VALUE.index(a)))

    def __check_for_pairs(self) -> HandPair | HandTwoPairs | None:
        doubles = ''
        for card in set(self.__sorted_hand):
            if self.__sorted_hand.count(card) == 2:
                doubles += card

        if len(doubles) == 1:
            return HandPair(doubles, self.__sorted_hand)
        elif len(doubles) == 2:
            return HandTwoPairs(*doubles, self.__sorted_hand)

        return None

    def __check_for_three_of_a_kind(self) -> HandThreeOfAKind | None:
        for card in set(self.__sorted_hand):
            if self.__sorted_hand.count(card) == 3:
                return HandThreeOfAKind(card, self.__sorted_hand)
        return None

    def __check_for_straight(self) -> HandStraight | None:
        if self.__sorted_hand in self.CARD_VALUE:
            return HandStraight(self.__sorted_hand)
        elif self.__sorted_hand == '2345A':
            return HandStraight('A2345')
        return None

    def __check_for_flush(self) -> HandFlush | None:
        if len(set(self.__get_hand_suit())) == 1:
            return HandFlush(self.__sorted_hand)
        return None

    def __check_for_full_house(self) -> HandFullHouse | None:
        three_of_a_kind = self.__check_for_three_of_a_kind()
        pair = self.__check_for_pairs()
        if three_of_a_kind and pair:
            return HandFullHouse(three_of_a_kind, pair)
        return None

    def __check_for_four_of_a_kind(self) -> HandFourOfAKind | None:
        for card in set(self.__sorted_hand):
            if self.__sorted_hand.count(card) == 4:
                return HandFourOfAKind(card, self.__sorted_hand)
        return None

    def __check_for_straight_flush(self) -> HandStraightFlush | None:
        straight = self.__check_for_straight()
        flush = self.__check_for_flush()
        if straight and flush:
            return HandStraightFlush(self.__sorted_hand)
        return None

    def __check_for_flush_royal(self) -> HandFlushRoyal | None:
        if 'TJQKA' == self.__sorted_hand and self.__check_for_flush():
            return HandFlushRoyal(self.__sorted_hand)
        return None

    def __get_hand_value(self):

        hand_value = self.__check_for_flush_royal()
        if hand_value:
            return hand_value

        hand_value = self.__check_for_straight_flush()
        if hand_value:
            return hand_value

        hand_value = self.__check_for_four_of_a_kind()
        if hand_value:
            return hand_value

        hand_value = self.__check_for_full_house()
        if hand_value:
            return hand_value

        hand_value = self.__check_for_flush()
        if hand_value:
            return hand_value

        hand_value = self.__check_for_straight()
        if hand_value:
            return hand_value

        hand_value = self.__check_for_three_of_a_kind()
        if hand_value:
            return hand_value

        hand_value = self.__check_for_pairs()
        if hand_value:
            return hand_value

        return HandHighCard(self.__sorted_hand)
