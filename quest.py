import sys, time
import random
import aspects as a
import utilities as util



##------------------------------
## METHOD DEFINITIONS
##------------------------------
def quest_generator():
    ## Create a template statement
    adjective=random.choice(a.adjectives)
    npc_type=random.choice(a.npc_types)
    objective=random.choice(a.objectives)
    location=random.choice(a.locations)
    obstacle=random.choice(a.obstacles)
    reward=random.choice(a.rewards)

    quest = f'''A {adjective} {npc_type} has contacted you with an urgent request. They need you to {objective} in {location}, but beware — you will need to deal with {obstacle}. If you succeed, you will be rewarded with {reward}.
'''
    return quest

def print_quest(quest):
    
    border = 65*'-'
    util.printer(border, 'fast')
    util.printer('INCOMING TRANSMISSION', 'fast')
    util.printer(border, 'fast')
    util.printer(util.wrap_text(quest, 'indent_all'))

##------------------------------
## TESTING
##------------------------------
def main():
    print('This is for testing only')
    print(2*'\n')
    # print(character_generator())
    quest = quest_generator()
    print_quest(quest)

    num_players = 2

    print(2*'\n')
    # print(50*'-')
    # print(2*'\n')

if __name__ == "__main__":
    main()
