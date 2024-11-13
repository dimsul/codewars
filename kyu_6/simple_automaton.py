# Description:
#
# Create a finite automaton that has three states. Finite automatons are
# the same as finite state machines for our purposes.
#
# Our simple automaton, accepts the language of A, defined as {0, 1} and
# should have three states: q1, q2, and q3. Here is the description of the states:
#
#     q1 is our start state, we begin reading commands from here
#     q2 is our accept state, we return true if this is our last state
#
# And the transitions:
#
#     q1 moves to q2 when given a 1, and stays at q1 when given a 0
#     q2 moves to q3 when given a 0, and stays at q2 when given a 1
#     q3 moves to q2 when given a 0 or 1
#
# The automaton should return whether we end in our accepted state (q2),
# or not (true/false).
#
# Your task
#
# You will have to design your state objects, and how your Automaton handles
# transitions. Also make sure you set up the three states, q1, q2, and q3
# for the myAutomaton instance. The test fixtures will be calling against myAutomaton.
#
# As an aside, the automaton accepts an array of strings, rather than just
# numbers, or a number represented as a string, because the language an
# automaton can accept isn't confined to just numbers. An automaton should
# be able to accept any 'symbol.'


class Automaton(object):

    def __init__(self):
        self.__current_stage = 'q1'

    def read_commands(self, commands):

        for command in commands:
            if self.__current_stage == 'q1':
                self.__q1_move(command)
            elif self.__current_stage == 'q2':
                self.__q2_move(command)
            else:
                self.__q3_move()

        if self.__current_stage == 'q2':
            return True

        return False

    def __q1_move(self, command):
        if command == '1':
            self.__current_stage = 'q2'

    def __q2_move(self, command):
        if command == '0':
            self.__current_stage = 'q3'

    def __q3_move(self):
        self.__current_stage = 'q2'
