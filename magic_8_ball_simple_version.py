# "Magic 8-Ball" in Python 2.7 -- one page version

import random

my_secrets = ["Yes", "No", "Maybe", "Who knows?", "It doesn't matter."]

global i_am_bored, i_feel_indecisive,i_am_relying_on_fate
i_am_bored = True
i_feel_indecisive = True
i_am_relying_on_fate = True

def ask_a_question():
    return raw_input("Hm... ")

def toss_the_8_ball():
    the_answer = what_i_want()
    print "The answer is... " + the_answer

def experience_a_mood_swing():
    global i_am_bored, i_feel_indecisive,i_am_relying_on_fate
    [i_am_bored, i_feel_indecisive, i_am_relying_on_fate] = fate_decides()

def what_i_want():
    a_random_thought = random.randint(0, len(my_secrets)-1)
    the_possibilities = my_secrets[a_random_thought]
    return the_possibilities

def fate_decides():
    one = yes_or_no()
    two = yes_or_no()
    three = yes_or_no()
    the_future = [one, two, three]
    return the_future

def yes_or_no():
    return random.randint(0, 1)

while i_am_bored or i_feel_indecisive or i_am_relying_on_fate:
    ask_a_question()
    toss_the_8_ball()
    experience_a_mood_swing()
